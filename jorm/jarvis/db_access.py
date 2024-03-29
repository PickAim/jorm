from abc import ABC, abstractmethod

from jorm.market.infrastructure import Niche, Warehouse, Marketplace, Category
from jorm.market.items import Product
from jorm.market.person import Account, User
from jorm.market.service import SimpleEconomySaveObject, TransitEconomySaveObject
from jorm.server.token.types import TokenType
from jorm.support.calculation import GreenTradeZoneCalculateResult, NicheCharacteristicsCalculateResult
from jorm.support.types import EconomyConstants


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
    def get_economy_constants(self, marketplace_id: int) -> EconomyConstants | None:
        pass

    @abstractmethod
    def get_warehouse(self, warehouse_id: int) -> Warehouse | None:
        pass

    @abstractmethod
    def get_all_warehouses(self, marketplace_id: int) -> dict[int, Warehouse]:
        pass

    @abstractmethod
    def get_all_warehouses_atomic(self, marketplace_id: int) -> dict[int, Warehouse]:
        pass

    @abstractmethod
    def get_products_by_user(self, user_id: int, marketplace_id: int) -> dict[int, Product]:
        pass

    @abstractmethod
    def get_products_by_user_atomic(self, user_id: int, marketplace_id: int) -> dict[int, Product]:
        pass

    @abstractmethod
    def get_users_warehouses(self, user_id: int, marketplace_id: int) -> dict[int, Warehouse]:
        pass

    @abstractmethod
    def get_all_simple_economy_results(self, user_id: int) -> list[SimpleEconomySaveObject]:
        pass

    @abstractmethod
    def get_all_transit_economy_results(self, user_id: int) -> list[TransitEconomySaveObject]:
        pass

    @abstractmethod
    def get_all_marketplaces(self) -> dict[int, Marketplace]:
        pass

    @abstractmethod
    def get_all_categories(self, marketplace_id: int) -> dict[int, Category]:
        pass

    @abstractmethod
    def get_all_niches(self, category_id: int) -> dict[int, Niche]:
        pass

    @abstractmethod
    def get_all_marketplaces_atomic(self) -> dict[int, Marketplace]:
        pass

    @abstractmethod
    def get_all_categories_atomic(self, marketplace_id: int) -> dict[int, Category]:
        pass

    @abstractmethod
    def get_all_niches_atomic(self, category_id: int) -> dict[int, Niche]:
        pass

    @abstractmethod
    def get_niche(self, niche_name: str, category_id: int, marketplace_id: int) -> Niche | None:
        pass

    @abstractmethod
    def get_niche_by_id(self, niche_id: int) -> Niche | None:
        pass

    @abstractmethod
    def get_niche_without_history(self, niche_id: int) -> Niche | None:
        pass

    @abstractmethod
    def get_green_zone_cache(self, niche_id: int) -> GreenTradeZoneCalculateResult | None:
        pass

    @abstractmethod
    def get_niche_characteristics_cache(self, niche_id: int) -> NicheCharacteristicsCalculateResult | None:
        pass
