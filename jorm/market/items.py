import datetime as date_root
from datetime import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from jorm.support.constants import DAYS_IN_MONTH
from jorm.support.types import StorageDict, SpecifiedTopPlace, SpecifiedLeftover, SpecMap, \
    DownturnSumCount
from jorm.support.utils import intersection


@dataclass
class ProductHistoryUnit:
    cost: int
    unit_date: datetime
    leftover: StorageDict

    def __str__(self) -> str:
        return f'{self.unit_date}: cost - {self.cost}; leftover - {str(self.leftover)};'


@dataclass
class ProductHistory:
    __history: list[ProductHistoryUnit] = field(default_factory=list)

    def __str__(self) -> str:
        return '\n'.join([str(unit) for unit in self.__history])

    def __post_init__(self):
        self.__history = sorted(self.__history, key=lambda unit: unit.unit_date)

    def __getitem__(self, idx: int):
        return self.__history[idx]

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
        end_idx = len(self.__history) - 1
        while self.__history[end_idx].unit_date > from_date:
            end_idx -= 1
        end_date = from_date - date_root.timedelta(DAYS_IN_MONTH)

        start_idx = 0
        while self.__history[start_idx].unit_date < end_date:
            start_idx += 1
        return start_idx, end_idx

    def get_all_leftovers(self) -> dict[int, SpecifiedLeftover]:
        last_history_unit: ProductHistoryUnit = self.__history[-1]
        warehouse_id_to_leftover: dict[int, SpecifiedLeftover] = {
            warehouse_id: last_history_unit.leftover[warehouse_id]
            for warehouse_id in last_history_unit.leftover
        }
        return warehouse_id_to_leftover

    def get_leftovers_downturn(self, from_date: datetime = datetime.utcnow()) -> dict[int, SpecMap]:
        start_idx, end_idx = self.__get_date_indexes(from_date)
        if start_idx >= end_idx:
            all_leftovers = self.get_all_leftovers()
            return {
                warehouse_id: SpecMap({all_leftovers[warehouse_id].specify: DownturnSumCount})
                for warehouse_id in all_leftovers
            }

        downturn_counts: dict[int, SpecMap] = {}
        for i in range(start_idx, min(end_idx, len(self.__history) - 1)):
            cur_unit = self.__history[i].leftover
            next_unit = self.__history[i + 1].leftover
            intersection_of_warehouse_id = intersection(cur_unit.keys(), next_unit.keys())
            for warehouse_id in intersection_of_warehouse_id:
                if warehouse_id not in downturn_counts:
                    downturn_counts[warehouse_id] = SpecMap()
                cur_specifies: dict[str, SpecifiedLeftover] = {
                    specify.specify: specify for specify in cur_unit[warehouse_id]
                }
                next_specifies: dict[str, SpecifiedLeftover] = {
                    specify.specify: specify for specify in next_unit[warehouse_id]
                }
                for specify in cur_specifies.keys():
                    next_leftover = next_specifies[specify].leftover if specify in next_specifies else 0
                    if next_leftover - cur_specifies[specify].leftover < 0:
                        if specify not in downturn_counts[warehouse_id]:
                            downturn_counts[warehouse_id][specify] = DownturnSumCount()
                        cur_downturn = downturn_counts[warehouse_id][specify]
                        cur_downturn.count += 1
                        cur_downturn.sum += next_leftover - cur_specifies[specify].leftover
        return downturn_counts


@dataclass
class ProductBase(ABC):
    name: str
    cost: int
    global_id: int
    rating: float


@dataclass
class ProductDefaultBase(ABC):
    history: ProductHistory = field(default_factory=ProductHistory)
    top_places: list[SpecifiedTopPlace] = field(default_factory=list)
    width: float = 0
    height: float = 0
    depth: float = 0


@dataclass
class Product(ProductDefaultBase, ProductBase):
    def __str__(self) -> str:
        return f'{self.name} ({self.global_id})'

    def get_my_volume(self) -> float:
        return self.width * self.height * self.depth * 1000


@dataclass
class ClientProductBase(ProductBase):
    niche_name: str
    category_name: str


@dataclass
class ClientProductDefaultBase(ProductDefaultBase):
    pass


@dataclass
class ClientProduct(ClientProductDefaultBase, Product, ClientProductBase):
    pass


@dataclass
class MarketplaceProduct(Product):
    pass
