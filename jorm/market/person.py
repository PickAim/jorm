from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

from .infrastructure import ClientMarketplace
from .infrastructure import Warehouse
from .service import Result


@dataclass
class ClientInfo:
    request_history: list[Result] = field(default_factory=list)
    marketplaces: list[ClientMarketplace] = field(default_factory=list)
    warehouses: list[Warehouse] = field(default_factory=list)
    profit_tax: float = 0.0


@dataclass
class Account:
    phone: str
    email: str
    hashed_password: str
    phone_number: str = ""


@dataclass
class User(ABC):
    user_id: int = -1
    name: str = "UNNAMED"

    def __str__(self) -> str:
        return self.name


@dataclass
class Admin(User):
    pass


class ClientPrivilege(Enum):
    DUNGEON_MASTER = 0
    BASIC = 1
    ADVANCED = 2
    PRO = 3


@dataclass
class Client(User):
    privilege: ClientPrivilege = ClientPrivilege.BASIC
    client_info: ClientInfo = field(default_factory=ClientInfo)

    def get_request_history(self) -> list[Result]:
        return self.client_info.request_history

    def get_marketplaces(self) -> list[ClientMarketplace]:
        return self.client_info.marketplaces

    def get_warehouses(self) -> list[Warehouse]:
        return self.client_info.warehouses

    def get_profit_tax(self) -> float:
        return self.client_info.profit_tax


@dataclass
class LowPayClient(Client):
    pass


@dataclass
class MiddlePayClient(Client):
    pass


@dataclass
class HighPayClient(Client):
    pass
