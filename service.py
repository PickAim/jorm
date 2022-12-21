from dataclasses import dataclass
from datetime import date


@dataclass
class Request:
    date: date

    def __init__(self, request_date: date):
        self.__date: date = request_date

    def __str__(self) -> str:
        return f'[{self.date}] {self.__class__.__name__}'


@dataclass
class EconomyRequest(Request):
    niche_name: str
    prime_cost: int
    pack_cost: int
    transit_cost: int
    transit_count: int


@dataclass
class FrequencyRequest(Request):
    search_str: str


@dataclass
class Result:
    request: Request


@dataclass
class EconomyResult(Result):
    commission: int
    margin: int
    transit_price: int
    storage_price: int
    logistic_price: int


class FrequencyResult(Result):
    frequencies: dict[int, int]

    def get_graph_coordinates(self) -> tuple[list[int], list[int]]:
        x = [self.frequencies[key] for key in self.frequencies.keys()]
        y = [self.frequencies[key] for key in self.frequencies.values()]
        return x, y
