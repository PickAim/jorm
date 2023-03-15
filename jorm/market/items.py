import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date

from jorm.support.constants import DAYS_IN_MONTH
from jorm.support.types import StorageDict


@dataclass
class ProductHistoryUnit:
    cost: int
    unit_date: datetime
    leftover: StorageDict

    def __str__(self) -> str:
        return f'{self.unit_date}: cost - {self.cost}; leftover - {str(self.leftover)};'


@dataclass
class ProductHistory:
    history: list[ProductHistoryUnit] = field(default_factory=list)

    def __str__(self) -> str:
        return '\n'.join([str(unit) for unit in self.history])

    def get_costs_pairs(self) -> dict[date, int]:
        return {unit.unit_date: unit.cost for unit in self.history}

    def get_leftovers_pairs(self) -> dict[date, int]:
        return {unit.unit_date: unit.leftover for unit in self.history}

    def get_last_month_trade_count(self, from_date: datetime.datetime) -> int:
        result: int = 0
        sorted_history = sorted(self.history, key=lambda unit: unit.unit_date)
        prev_value = 0
        for history_unit in sorted_history:
            if abs((from_date - history_unit.unit_date).days) < DAYS_IN_MONTH:
                if prev_value > history_unit.leftover.get_all_leftovers():
                    result += prev_value - history_unit.leftover.get_all_leftovers()
                prev_value = history_unit.leftover.get_all_leftovers()
        return result


@dataclass
class ProductBase(ABC):
    name: str
    cost: int
    article: int


@dataclass
class ProductDefaultBase(ABC):
    history: ProductHistory = field(default_factory=ProductHistory)
    width: float = 0
    height: float = 0
    depth: float = 0


@dataclass
class Product(ProductDefaultBase, ProductBase):
    def __str__(self) -> str:
        return f'{self.name} ({self.article})'

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
