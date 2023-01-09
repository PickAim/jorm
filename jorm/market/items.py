from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date


@dataclass
class ProductHistoryUnit:
    cost: int
    leftover: int
    unit_date: date

    def __str__(self) -> str:
        return f'{self.unit_date}: cost - {self.cost}; leftover - {self.leftover};'


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
class Product(ABC):
    name: str
    cost: int
    article: int
    history: ProductHistory

    def __str__(self) -> str:
        return f'{self.name} ({self.article})'


@dataclass
class ClientProduct(Product):
    niche_name: str
    category_name: str


@dataclass
class MarketplaceProduct(Product):
    pass
