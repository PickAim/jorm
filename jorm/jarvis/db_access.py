from abc import ABC, abstractmethod

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
    def get_niche(self, niche_name: str) -> Niche | None:
        pass

    @abstractmethod
    def get_warehouse(self, warehouse_name: str) -> Warehouse | None:
        pass

    @abstractmethod
    def get_all_warehouses(self) -> list[Warehouse] | None:
        pass
