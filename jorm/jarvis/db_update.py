from abc import ABC, abstractmethod

from jorm.market.infrastructure import Niche

from jorm.market.service import UnitEconomyRequest, UnitEconomyResult, FrequencyRequest, FrequencyResult, RequestInfo

from jorm.market.person import User, Account


class UserInfoChanger(ABC):
    @abstractmethod
    def update_session_tokens(self, user_id: int, old_update_token: str,
                              new_access_token: str, new_update_token: str) -> None:
        # add exceptions
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
    def delete_tokens_for_user(self, user_id: int, imprint_token: str) -> None:
        pass


class JORMChanger(ABC):
    @abstractmethod
    def save_unit_economy_request(self, request: UnitEconomyRequest,
                                  result: UnitEconomyResult,
                                  request_info: RequestInfo,
                                  user_id: int) -> int:
        pass

    @abstractmethod
    def save_frequency_request(self, request: FrequencyRequest,
                               result: FrequencyResult,
                               request_info: RequestInfo,
                               user_id: int) -> int:
        pass

    @abstractmethod
    def delete_unit_economy_request(self, request_id: int, user_id: int) -> None:
        pass

    @abstractmethod
    def delete_frequency_request(self, request_id: int, user_id: int) -> None:
        pass

    @abstractmethod
    def load_new_niche(self, niche_name: str) -> Niche:
        pass
