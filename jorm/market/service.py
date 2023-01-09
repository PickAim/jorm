from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date


@dataclass
class Request(ABC):
    date: date

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
class Result(ABC):
    request: Request


@dataclass
class EconomyResult(Result):
    buy_cost: int
    pack_cost: int
    marketplace_commission: int
    logistic_price: int
    storage_price: int
    margin: int
    recommended_price: int
    transit_profit: int
    roi: int
    transit_margin_percent: float


@dataclass
class FrequencyResult(Result):
    frequencies: dict[int, int]

    def get_graph_coordinates(self) -> tuple[list[int], list[int]]:
        x, y = [], []
        for key in self.frequencies.keys():
            x.append(key)
            y.append(self.frequencies[key])
        return x, y
