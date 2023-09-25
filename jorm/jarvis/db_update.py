from abc import ABC, abstractmethod

from jorm.market.infrastructure import Niche, Warehouse
from jorm.market.items import Product
from jorm.market.person import User, Account
from jorm.market.service import SimpleEconomySaveObject, TransitEconomySaveObject
from jorm.support.calculation import GreenTradeZoneCalculateResult, NicheCharacteristicsCalculateResult
from jorm.support.types import EconomyConstants


class UserInfoChanger(ABC):
    @abstractmethod
    def update_session_tokens(self, user_id: int, old_update_token: str,
                              new_access_token: str, new_update_token: str) -> None:
        pass

    @abstractmethod
    def update_session_tokens_by_imprint(self, access_token: str,
                                         update_token: str, imprint_token: str, user_id: int) -> None:
        pass

    @abstractmethod
    def save_all_tokens(self, access_token: str, update_token: str, imprint_token: str, user_id: int) -> None:
        pass

    @abstractmethod
    def save_user_and_account(self, user: User, account: Account) -> None:
        pass

    @abstractmethod
    def add_marketplace_api_key(self, api_key: str, user_id: int, marketplace_id: int) -> None:
        pass

    @abstractmethod
    def delete_marketplace_api_key(self, user_id: int, marketplace_id: int) -> None:
        pass

    @abstractmethod
    def delete_account(self, user_id: int) -> None:
        pass

    @abstractmethod
    def delete_tokens_for_user(self, user_id: int, imprint_token: str) -> None:
        pass


class JORMChanger(ABC):
    @abstractmethod
    def update_niche(self, niche_id: int, category_id: int, marketplace_id: int) -> Niche:
        pass

    @abstractmethod
    def update_green_zone_cache(self, niche_id: int,
                                green_trade_zone_calc_result: GreenTradeZoneCalculateResult) -> None:
        pass

    @abstractmethod
    def update_niche_characteristics_cache(self, niche_id: int,
                                           niche_characteristics_calc_result: NicheCharacteristicsCalculateResult) \
            -> None:
        pass

    @abstractmethod
    def update_economy_constants(self, marketplace_id: int, economy_constants: EconomyConstants) -> None:
        pass

    @abstractmethod
    def save_simple_economy_request(self, save_object: SimpleEconomySaveObject, user_id: int) -> int:
        pass

    @abstractmethod
    def save_transit_economy_request(self, save_object: TransitEconomySaveObject, user_id: int) -> int:
        pass

    @abstractmethod
    def delete_simple_economy_request(self, request_id: int, user_id: int) -> None:
        pass

    @abstractmethod
    def delete_transit_economy_request(self, request_id: int, user_id: int) -> None:
        pass

    @abstractmethod
    def load_new_niche(self, niche_name: str, marketplace_id: int) -> Niche | None:
        pass

    @abstractmethod
    def load_user_products(self, user_id: int, marketplace_id: int) -> list[Product]:
        pass

    @abstractmethod
    def load_user_warehouse(self, user_id: int, marketplace_id: int) -> list[Warehouse]:
        pass
