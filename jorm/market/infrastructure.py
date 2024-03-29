from abc import ABC
from dataclasses import dataclass, field
from enum import Enum

import numpy as np
from numpy import ndarray

from jorm.support.constants import SAMPLES_COUNT
from .items import Product


class HandlerType(Enum):
    MARKETPLACE = "market"
    PARTIAL_CLIENT = "partial client"
    CLIENT = "client"


@dataclass
class Niche(ABC):
    name: str
    commissions: dict[HandlerType, float]
    returned_percent: float
    _products: list[Product] = field(default_factory=list)
    request_rate: int = 0

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products: list[Product]):
        self._products = products
        self.__calc_cost_data()

    def __str__(self) -> str:
        return self.name

    def __post_init__(self):
        self.__calc_cost_data()

    def __calc_cost_data(self):
        self.cost_data: ndarray = np.array(
            [product.cost for product in self.products])
        self.cost_data.sort()
        self.max_commission: float = max(
            [self.commissions[key] for key in self.commissions.keys()])

    def get_concurrent_margin(self,
                              mid_cost: float,
                              unit_cost: int,
                              basic_logistic_price: int,
                              basic_storage_cost: int) -> int:
        return int(mid_cost - unit_cost - self.max_commission * mid_cost - basic_logistic_price - basic_storage_cost)

    def get_mean_concurrent_cost(self,
                                 unit_cost: int,
                                 basic_logistic_price: int,
                                 basic_storage_price: int,
                                 samples_count: int = SAMPLES_COUNT) -> int:
        keys: list[int] = []
        if len(self.cost_data) > samples_count:
            step: int = len(self.cost_data) // samples_count
            for i in range(samples_count - 1):
                keys.append(i * step)
            keys.append(len(self.cost_data) - 1)
        elif len(self.cost_data) > 0:
            keys.extend([0, len(self.cost_data) - 1])
        else:
            return 0
        for i in range(1, len(keys)):
            concurrent_margin: int = self.get_concurrent_margin(self.cost_data[keys[i - 1]:keys[i]].mean(),
                                                                unit_cost, basic_logistic_price, basic_storage_price)
            if concurrent_margin > 0:
                return int(self.cost_data[keys[i - 1]:keys[i]].mean())
        return int(self.cost_data[-2:-1].mean())

    def get_mean_product_volume(self) -> float:
        if len(self.products) == 0:
            return 0
        summary_volume: float = 0
        for product in self.products:
            summary_volume += product.get_my_volume()
        return summary_volume / len(self.products)

    def get_commission(self, handler_type: HandlerType):
        return self.commissions[handler_type]


@dataclass
class Category(ABC):
    name: str
    niches: dict[str, Niche] = field(default_factory=dict)

    def __str__(self) -> str:
        return self.name

    def get_niche_by_name(self, niche_name: str) -> Niche:
        return self.niches[niche_name]


@dataclass
class Address(ABC):
    region: str
    street: str


@dataclass
class Warehouse(ABC):
    name: str
    global_id: int
    handler_type: HandlerType
    address: Address
    main_coefficient: float = 1.0
    products: list[Product] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name

    def get_niche_commission(self, niche: Niche) -> float:
        if niche is None:
            return 0.0
        return niche.commissions[self.handler_type]


@dataclass
class Marketplace(ABC):
    name: str
    warehouses: list[Warehouse] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name


@dataclass
class UnknownMarketplace(Marketplace):
    categories: dict[str, Category] = field(default_factory=dict)

    def get_category_by_name(self, category_name: str) -> Category:
        return self.categories[category_name]

    def get_niche_by_name(self, category_name: str, niche_name: str) -> Niche:
        return self.categories[category_name].get_niche_by_name(niche_name)
