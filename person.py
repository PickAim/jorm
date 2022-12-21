from market.infrastructure import ClientMarketplace
from market.infrastructure import Warehouse
from service import Result


class ClientInfo:
    def __init__(self, request_history: list[Result],
                 marketplaces: list[ClientMarketplace], warehouses: list[Warehouse]):
        self.__request_history: list[Result] = request_history
        self.__marketplaces: list[ClientMarketplace] = marketplaces
        self.__warehouses: list[Warehouse] = warehouses

    def get_request_history(self) -> list[Result]:
        return self.__request_history

    def get_marketplaces(self) -> list[ClientMarketplace]:
        return self.__marketplaces

    def get_warehouses(self) -> list[Warehouse]:
        return self.__warehouses


class User:
    def __init__(self, name: str):
        self.__name: str = name

    def __str__(self) -> str:
        return self.__name

    def get_name(self) -> str:
        return self.__name


class Admin(User):
    def __init__(self, name: str):
        super().__init__(name)


class Client(User):
    def __init__(self, name: str, client_info: ClientInfo):
        super().__init__(name)
        self.__client_info: ClientInfo = client_info

    def get_request_history(self) -> list[Result]:
        return self.__client_info.get_request_history()

    def get_marketplaces(self) -> list[ClientMarketplace]:
        return self.__client_info.get_marketplaces()

    def get_warehouses(self) -> list[Warehouse]:
        return self.__client_info.get_warehouses()


class LowPayClient(Client):
    def __init__(self, name: str, client_info: ClientInfo):
        super().__init__(name, client_info)


class MiddlePayClient(Client):
    def __init__(self, name: str, client_info: ClientInfo):
        super().__init__(name, client_info)


class HighPayClient(Client):
    def __init__(self, name: str, client_info: ClientInfo):
        super().__init__(name, client_info)
