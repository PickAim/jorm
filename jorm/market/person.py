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
    login: str
    hashed_password: bytes
    phone_number: str = ""


@dataclass
class User(ABC):
    name: str = "UNNAMED"

    def __str__(self) -> str:
        return self.name


@dataclass
class Admin(User):
    pass


class ClientPrivilege(Enum):
    DUNGEON_MASTER = 0
    BASIC: int = 1
    ADVANCED: int = 2
    PRO: int = 3


@dataclass
class Client(User):
    privilege: int = ClientPrivilege.BASIC
    client_info: ClientInfo = ClientInfo()

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
