from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from market.infrastructure import ClientMarketplace
from market.infrastructure import Warehouse
from service import Result


@dataclass
class ClientInfo:
    request_history: list[Result] = field(default_factory=list)
    marketplaces: list[ClientMarketplace] = field(default_factory=list)
    warehouses: list[Warehouse] = field(default_factory=list)
    profit_tax: float = 0.0


@dataclass
class User(ABC):
    name: str

    def __str__(self) -> str:
        return self.name


@dataclass
class Admin(User):
    pass


@dataclass
class Client(User):
    client_info: ClientInfo

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
