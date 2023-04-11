from abc import ABC, abstractmethod

from jorm.market.service import UnitEconomyRequest, UnitEconomyResult, RequestInfo

from jorm.market.items import Product

from jorm.server.token.types import TokenType

from jorm.market.infrastructure import Niche, Warehouse

from jorm.market.person import Account, User


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
    def get_niche(self, niche_name: str, marketplace_id: int) -> Niche | None:
        pass

    @abstractmethod
    def get_warehouse(self, warehouse_name: str) -> Warehouse | None:
        pass

    @abstractmethod
    def get_all_warehouses(self) -> list[Warehouse] | None:
        pass

    @abstractmethod
    def get_products_by_user(self, user: User) -> list[Product]:
        pass

    @abstractmethod
    def get_all_unit_economy_results(self, user: User) \
            -> list[tuple[UnitEconomyRequest, UnitEconomyResult, RequestInfo]]:
        pass
