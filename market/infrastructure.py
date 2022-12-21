from dataclasses import dataclass
from market.items import Product
from market.items import ClientProduct
from market.items import MarketplaceProduct


@dataclass
class Niche:
    name: str
    products: list[MarketplaceProduct]

    def __str__(self) -> str:
        return self.name


@dataclass
class Category:
    name: str
    niches: dict[str, Niche]

    def __str__(self) -> str:
        return self.name

    def get_niche_by_name(self, niche_name: str) -> Niche:
        return self.niches[niche_name]


@dataclass
class Address:
    # TODO think about fields declaration in this class (street, city, country, etc)
    address: str = ""


@dataclass
class Warehouse:
    name: str
    global_id: int
    commission: int
    address: Address
    products: list[Product] = None

    def __str__(self) -> str:
        return self.name


@dataclass
class Marketplace:
    name: str
    warehouses: list[Warehouse]

    def __str__(self) -> str:
        return self.name


class UnknownMarketplace(Marketplace):
    categories: dict[str, Category]

    def get_category_by_name(self, category_name: str) -> Category:
        return self.categories[category_name]

    def get_niche_by_name(self, category_name: str, niche_name: str) -> Niche:
        return self.categories[category_name].get_niche_by_name(niche_name)


class ClientMarketplace(Marketplace):
    products: list[ClientProduct]
