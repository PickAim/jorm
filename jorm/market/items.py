import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date

from jorm.support.types import StorageDict


@dataclass
class ProductHistoryUnit:
    cost: int
    unit_date: date
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
