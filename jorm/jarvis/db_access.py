from abc import ABC, abstractmethod

from jorm.market.infrastructure import Niche, Warehouse, Marketplace, Category
from jorm.market.items import Product
from jorm.market.person import Account, User
from jorm.market.service import UnitEconomyRequest, UnitEconomyResult, RequestInfo, FrequencyRequest, FrequencyResult
from jorm.server.token.types import TokenType


class UserInfoCollector(ABC):
    @abstractmethod
    def get_user_by_account(self, account: Account) -> User | None:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    def get_account_and_id(self, email: str, phone: str) -> tuple[Account, int] | None:
        pass

    @abstractmethod
    def get_token_rnd_part(self, user_id: int, imprint: str, token_type: TokenType) -> str:
        pass


class JORMCollector(ABC):
    @abstractmethod
    def get_warehouse(self, warehouse_name: str, marketplace_id: int) -> Warehouse | None:
        pass

    @abstractmethod
    def get_all_warehouses(self, marketplace_id: int) -> list[Warehouse]:
        pass

    @abstractmethod
    def get_products_by_user(self, user_id: int) -> list[Product]:
        pass

    @abstractmethod
    def get_users_warehouses(self, user_id: int, marketplace_id: int) -> list[Warehouse]:
        pass

    @abstractmethod
    def get_all_unit_economy_results(self, user_id: int) \
            -> list[tuple[UnitEconomyRequest, UnitEconomyResult, RequestInfo]]:
        pass

    @abstractmethod
    def get_all_frequency_results(self, user_id: int) \
            -> list[tuple[FrequencyRequest, FrequencyResult, RequestInfo]]:
        pass

    @abstractmethod
    def get_all_marketplaces(self) -> dict[int, Marketplace]:
        pass

    @abstractmethod
    def get_all_categories(self, marketplace_id: int) -> dict[int, Category]:
        pass

    @abstractmethod
    def get_niche(self, niche_name: str, category_name: str, marketplace_id: int) -> Niche | None:
        pass
