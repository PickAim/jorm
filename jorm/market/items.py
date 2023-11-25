import datetime as date_root
from datetime import datetime
from abc import ABC
from dataclasses import dataclass, field
from typing import Iterable

from jorm.support.constants import DAYS_IN_MONTH
from jorm.support.types import StorageDict, SpecifiedTopPlaceDict, SpecifiedLeftover, DownturnMap, \
    DownturnSumCount


@dataclass
class ProductHistoryUnit:
    cost: int
    unit_date: datetime
    leftover: StorageDict

    def __str__(self) -> str:
        return f'{self.unit_date}: cost - {self.cost}; leftover - {str(self.leftover)};'

    def __eq__(self, other) -> bool:
        if self.cost != other.cost:
            return False
        if self.unit_date != other.unit_date:
            return False
        if self.leftover != other.leftover:
            return False
        return True


class ProductHistory:
    def __init__(self, history: Iterable[ProductHistoryUnit] | None = None):
        if history is None:
            history = []
        self.__history = list(history)

    def __str__(self) -> str:
        return '\n'.join([str(unit) for unit in self.__history])

    def __eq__(self, other):
        other_history: list[ProductHistoryUnit] = other.get_history()
        if len(self.__history) != len(other.get_history()):
            return False
        for i in range(len(self.__history)):
            if self.__history[i] != other_history[i]:
                return False
        return True

    def __post_init__(self):
        self.__history = sorted(
            self.__history, key=lambda unit: unit.unit_date)

    def __getitem__(self, idx: int):
        return self.__history[idx]

    def get_history(self) -> list[ProductHistoryUnit]:
        return list(self.__history)

    def add(self, history_unit: ProductHistoryUnit):
        for i in range(len(self.__history) - 1, -1, -1):
            if self.__history[i].unit_date > history_unit.unit_date:
                self.__history.insert(i, history_unit)
                return
        self.__history.insert(len(self.__history), history_unit)

    def get_costs_pairs(self) -> dict[datetime, int]:
        return {unit.unit_date: unit.cost for unit in self.__history}

    def get_leftovers_pairs(self) -> dict[datetime, StorageDict]:
        return {unit.unit_date: unit.leftover for unit in self.__history}

    def get_last_month_trade_count(self, from_date: datetime = datetime.utcnow()) -> int:
        start_idx, end_idx = self.__get_date_indexes(from_date)
        if start_idx >= end_idx:
            return 0
        return self.__calc_trade_count(start_idx, end_idx)

    def __calc_trade_count(self, start_idx: int, end_idx: int) -> int:
        prev_value = 0
        result: int = 0
        for history_unit in self.__history[start_idx: end_idx + 1]:
            leftover = history_unit.leftover.get_all_leftovers()
            if prev_value > leftover >= 0:
                result += prev_value - leftover
            prev_value = leftover
        return result

    def __get_date_indexes(self, from_date: datetime) -> tuple[int, int]:
        self.__history = sorted(self.__history, key=lambda unit: unit.unit_date)
        if len(self.__history) == 0:
            return -1, -1
        end_idx = len(self.__history) - 1
        # two element ass minimum
        while self.__history[end_idx].unit_date > from_date and end_idx > 1:
            end_idx -= 1
        end_date = from_date - date_root.timedelta(DAYS_IN_MONTH)

        start_idx = 0
        while self.__history[start_idx].unit_date < end_date \
                and start_idx < len(self.__history) - 2:  # two element ass minimum
            start_idx += 1
        return start_idx, end_idx

    def get_all_leftovers(self) -> dict[int, list[SpecifiedLeftover]]:
        if len(self.__history) == 0:
            return {}
        last_history_unit: ProductHistoryUnit = self.__history[-1]
        warehouse_id_to_leftover: dict[int, list[SpecifiedLeftover]] = {
            warehouse_id: last_history_unit.leftover[warehouse_id]
            for warehouse_id in last_history_unit.leftover
        }
        return warehouse_id_to_leftover

    def get_all_mapped_leftovers(self) -> dict[int, dict[str, int]]:
        if len(self.__history) == 0:
            return {}
        last_history_unit: ProductHistoryUnit = self.__history[-1]
        return last_history_unit.leftover.get_mapped_leftovers()

    def get_leftovers_downturn(self, from_date: datetime = datetime.utcnow()) -> dict[int, DownturnMap]:
        start_idx, end_idx = self.__get_date_indexes(from_date)
        if start_idx >= end_idx:
            all_leftovers: dict[int, list[SpecifiedLeftover]
                                ] = self.get_all_leftovers()
            return {
                warehouse_id: DownturnMap({
                    specify_obj.specify: DownturnSumCount()
                    for specify_obj in all_leftovers[warehouse_id]
                })
                for warehouse_id in all_leftovers
            }

        downturn_counts: dict[int, DownturnMap] = {}
        for i in range(start_idx, min(end_idx, len(self.__history) - 1)):
            cur_unit = self.__history[i].leftover
            next_unit = self.__history[i + 1].leftover
            cur_specifies: dict[int, dict[str, int]
                                ] = cur_unit.get_mapped_leftovers()
            next_specifies: dict[int, dict[str, int]
                                 ] = next_unit.get_mapped_leftovers()
            for warehouse_id in cur_specifies:
                if warehouse_id not in downturn_counts:
                    downturn_counts[warehouse_id] = DownturnMap()
                for specify in cur_specifies[warehouse_id]:
                    next_leftover = next_specifies[warehouse_id][specify] \
                        if warehouse_id in next_specifies and specify in next_specifies[warehouse_id] \
                        else 0
                    if next_leftover - cur_specifies[warehouse_id][specify] <= 0:
                        if specify not in downturn_counts[warehouse_id]:
                            downturn_counts[warehouse_id][specify] = DownturnSumCount(
                            )
                        cur_downturn = downturn_counts[warehouse_id][specify]
                        cur_downturn.count += 1
                        cur_downturn.sum += next_leftover - \
                            cur_specifies[warehouse_id][specify]
        return downturn_counts


@dataclass
class ProductBase(ABC):
    name: str
    cost: int
    global_id: int
    rating: float
    brand: str
    seller: str
    category_niche_list: list[tuple[str, str]]


@dataclass
class ProductDefaultBase(ABC):
    history: ProductHistory = field(default_factory=ProductHistory)
    top_places: SpecifiedTopPlaceDict = field(default_factory=SpecifiedTopPlaceDict)
    width: float = 0
    height: float = 0
    depth: float = 0


@dataclass
class Product(ProductDefaultBase, ProductBase):
    def __str__(self) -> str:
        return f'{self.name} ({self.global_id})'

    def get_my_volume(self) -> float:
        return self.width * self.height * self.depth * 1000
