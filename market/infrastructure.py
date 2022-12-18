from market.items import Product
from market.items import ClientProduct
from market.items import MarketplaceProduct


class Niche:
    def __init__(self, name: str, products: list[MarketplaceProduct]):
        self.__name: str = name
        self.__products: list[MarketplaceProduct] = products

    def __str__(self) -> str:
        return self.__name

    def get_products(self) -> list[MarketplaceProduct]:
        return self.__products


class Category:
    def __init__(self, name: str, niches: dict[str, Niche]):
        self.__name: str = name
        self.__niches: dict[str, Niche] = niches

    def __str__(self) -> str:
        return self.__name

    def get_niches(self) -> dict[str, Niche]:
        return self.__niches

    def get_niche_by_name(self, niche_name: str) -> Niche:
        return self.__niches[niche_name]


class Address:
    def __init__(self):
        self.address: str = ""  # TODO think about fields declaration in this class (street, city, country, etc)


class Warehouse:
    def __init__(self, name: str, global_id: int, commission: int, address: Address, products: list[Product] = None):
        self.__name: str = name
        self.__global_id: int = global_id
        self.__commission: int = commission
        self.__address: Address = address
        self.__products: list[Product] = products

    def __str__(self) -> str:
        return self.__name

    def get_name(self) -> str:
        return self.__name

    def get_global_id(self) -> int:
        return self.__global_id

    def get_commission(self) -> int:
        return self.__commission

    def get_address(self) -> Address:
        return self.__address

    def set_products(self, products: list[Product]):
        self.__products = products

    def get_products(self) -> list[Product]:
        return self.__products


class Marketplace:
    def __init__(self, name: str, warehouses: list[Warehouse]):
        self.__name: str = name
        self.__warehouses: list[Warehouse] = warehouses

    def __str__(self) -> str:
        return self.__name

    def get_name(self) -> str:
        return self.__name

    def get_warehouses(self) -> list[Warehouse]:
        return self.__warehouses


class UnknownMarketplace(Marketplace):
    def __init__(self, name: str, warehouses: list[Warehouse], category: dict[str, Category]):
        super().__init__(name, warehouses)
        self.__categories: dict[str, Category] = category

    def get_categories(self) -> dict[str, Category]:
        return self.__categories

    def get_category_by_name(self, category_name: str) -> Category:
        return self.__categories[category_name]

    def get_niche_by_name(self, category_name: str, niche_name: str) -> Niche:
        return self.__categories[category_name].get_niche_by_name(niche_name)


class ClientMarketplace(Marketplace):
    def __init__(self, name: str, warehouses: list[Warehouse], products: list[ClientProduct]):
        super().__init__(name, warehouses)
        self.__products: list[ClientProduct] = products

    def get_products(self) -> list[Product]:
        return self.__products
