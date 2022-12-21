from dataclasses import dataclass
from datetime import date


@dataclass
class ProductHistoryUnit:
    cost: int
    leftover: int
    unit_date: date

    def __str__(self) -> str:
        return f'{self.unit_date} : cost {self.cost}; leftover - {self.leftover};'


class ProductHistory:
    def __init__(self, history: list[ProductHistoryUnit]):
        self.__history: list[ProductHistoryUnit] = history

    def __str__(self) -> str:
        result = ""
        for unit in self.__history:
            result += unit.__str__()
        return result

    def get_costs_pairs(self) -> dict[date, int]:
        return {unit.get_date: unit.get_cost for unit in self.__history}

    def get_leftovers_pairs(self) -> dict[date, int]:
        return {unit.get_date: unit.get_leftover() for unit in self.__history}


@dataclass
class Product:
    name: str
    cost: int
    article: int
    history: ProductHistory

    def __str__(self) -> str:
        return f'{self.name} ({self.article})'


class ClientProduct(Product):
    niche_name: str
    category_name: str


class MarketplaceProduct(Product):
    pass
