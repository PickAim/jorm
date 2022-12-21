from dataclasses import dataclass
from market.infrastructure import ClientMarketplace
from market.infrastructure import Warehouse
from service import Result


@dataclass
class ClientInfo:
    request_history: list[Result]
    marketplaces: list[ClientMarketplace]
    warehouses: list[Warehouse]


@dataclass
class User:
    name: str

    def __str__(self) -> str:
        return self.name


@dataclass
class Admin(User):
    pass


@dataclass
class Client(User):
    name: str
    client_info: ClientInfo

    def get_request_history(self) -> list[Result]:
        return self.client_info.request_history

    def get_marketplaces(self) -> list[ClientMarketplace]:
        return self.client_info.marketplaces

    def get_warehouses(self) -> list[Warehouse]:
        return self.client_info.warehouses


@dataclass
class LowPayClient(Client):
    pass


@dataclass
class MiddlePayClient(Client):
    pass


@dataclass
class HighPayClient(Client):
    pass
