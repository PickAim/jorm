from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

import numpy as np
from numpy import ndarray

from .constants import samples_count
from .items import Product
from .items import ClientProduct
from .items import MarketplaceProduct


class HandlerType(Enum):
    MARKETPLACE = "market"
    PARTIAL_CLIENT = "partial client"
    CLIENT = "client"


@dataclass
class Niche(ABC):
    name: str
    commissions: dict[HandlerType, float]
    returned_percent: float
    products: list[Product] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name

    def __post_init__(self):
        self.cost_data: ndarray = np.array([product.cost for product in self.products])
        self.cost_data.sort()
        self.max_commission: float = max([self.commissions[key] for key in self.commissions.keys()])

    def get_concurrent_margin(self,
                              mid_cost: float,
                              unit_cost: int,
                              basic_logistic_price: int,
                              basic_storage_cost: int) -> int:
        return int(mid_cost - unit_cost - self.max_commission * mid_cost - basic_logistic_price - basic_storage_cost)

    def get_mean_concurrent_cost(self,
                                 unit_cost: int,
                                 basic_logistic_price: int,
                                 basic_storage_price: int) -> int:
        keys: list[int] = []
        if len(self.cost_data) > samples_count:
            step: int = len(self.cost_data) // samples_count
            for i in range(samples_count - 1):
                keys.append(i * step)
            keys.append(len(self.cost_data) - 1)
        else:
            keys.extend([0, len(self.cost_data) - 1])
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
class MarketplaceNiche(Niche):
    products: list[MarketplaceProduct] = field(default_factory=list)


@dataclass
class Category(ABC):
    name: str
    niches: dict[str, Niche] = field(default_factory=list)

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
    handler_type: HandlerType
    address: Address
    products: list[Product] = field(default_factory=list)
    basic_logistic_to_customer_commission: int = 0
    additional_logistic_to_customer_commission: float = 0
    logistic_from_customer_commission: int = 0
    basic_storage_commission: int = 0
    additional_storage_commission: float = 0
    mono_palette_storage_commission: int = 0

    def __str__(self) -> str:
        return self.name

    def get_niche_commission(self, niche: Niche) -> float:
        return niche.commissions[self.handler_type]

    def calculate_logistic_to_customer_price(self, liters: float) -> int:
        return int(self.basic_logistic_to_customer_commission
                   + self.additional_logistic_to_customer_commission * liters)

    def calculate_logistic_from_customer_price(self) -> int:
        return self.logistic_from_customer_commission

    def calculate_storage_price(self, liters: float) -> int:
        return int(self.basic_storage_commission
                   + self.additional_storage_commission * liters)

    def calculate_logistic_price_for_one(self, liters: float, returns_percent: float) -> int:
        return self.calculate_logistic_to_customer_price(liters) \
               + int(self.calculate_logistic_from_customer_price() * returns_percent)


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
    products: list[ClientProduct] = field(default_factory=list)
