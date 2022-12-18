from market.items import MarketplaceProduct
from market.items import Product


class Niche:
    def __init__(self, name: str, products: dict[str, MarketplaceProduct]):
        self.__name: str = name
        self.__products: dict[str, MarketplaceProduct] = products

    def __str__(self) -> str:
        return self.__name

    def get_products(self) -> dict[str, MarketplaceProduct]:
        return self.__products


class Category:
    def __init__(self, name: str, niches: dict[str, Niche]):
        self.__name: str = name
        self.__niches: dict[str, Niche] = niches

    def __str__(self) -> str:
        return self.__name

    def get_niches(self) -> dict[str, Niche]:
        return self.__niches


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
