from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np
from numpy import ndarray

from .constants import samples_count
from .items import Product
from .items import ClientProduct
from .items import MarketplaceProduct


@dataclass
class Niche(ABC):
    name: str
    commission: float
    logistic_price: int
    returned_percent: float
    products: list[Product]

    def __str__(self) -> str:
        return self.name

    def __post_init__(self):
        self.cost_data: ndarray = np.array([product.cost for product in self.products])

    def get_concurrent_margin(self,
                              mid_cost: float,
                              unit_cost: int,
                              unit_storage_cost: int) -> int:
        return int(mid_cost - unit_cost - self.commission * mid_cost - self.logistic_price - unit_storage_cost)

    def get_mean_concurrent_cost(self,
                                 unit_cost: int,
                                 storage_price: int) -> int:
        keys: list[int] = []
        step: int = len(self.cost_data) // samples_count
        for i in range(samples_count - 1):
            keys.append(i * step)
        keys.append(len(self.cost_data) - 1)
        for i in range(1, len(keys)):
            concurrent_margin: int = self.get_concurrent_margin(self.cost_data[keys[i - 1]:keys[i]].mean(), unit_cost,
                                                                storage_price)
            if concurrent_margin > 0:
                return int(self.cost_data[keys[i - 1]:keys[i]].mean())
        return int(self.cost_data[-2:-1].mean())


@dataclass
class MarketplaceNiche(Niche):
    products: list[MarketplaceProduct]


@dataclass
class Category(ABC):
    name: str
    niches: dict[str, Niche]

    def __str__(self) -> str:
        return self.name

    def get_niche_by_name(self, niche_name: str) -> Niche:
        return self.niches[niche_name]


@dataclass
class Address(ABC):
    # TODO think about fields declaration in this class (street, city, country, etc)
    address: str = ""


@dataclass
class Warehouse(ABC):
    name: str
    global_id: int
    commission: int
    address: Address
    products: list[Product]

    def __str__(self) -> str:
        return self.name


@dataclass
class Marketplace(ABC):
    name: str
    warehouses: list[Warehouse]

    def __str__(self) -> str:
        return self.name


@dataclass
class UnknownMarketplace(Marketplace):
    categories: dict[str, Category]

    def get_category_by_name(self, category_name: str) -> Category:
        return self.categories[category_name]

    def get_niche_by_name(self, category_name: str, niche_name: str) -> Niche:
        return self.categories[category_name].get_niche_by_name(niche_name)


@dataclass
class ClientMarketplace(Marketplace):
    products: list[ClientProduct]
