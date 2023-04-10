from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from jorm.support.bases.service import __UnitEconomyRequestDefaultBase, __UnitEconomyRequestBase, \
    __FrequencyRequestDefaultBase, __FrequencyRequestBase


class RequestInfo:
    id: int = -1
    date: datetime = datetime.utcnow()
    name: str = ""


@dataclass
class Request(ABC):
    info: RequestInfo = RequestInfo()


@dataclass
class UnitEconomyRequest(Request, __UnitEconomyRequestDefaultBase, __UnitEconomyRequestBase):
    pass


@dataclass
class FrequencyRequest(Request, __FrequencyRequestDefaultBase, __FrequencyRequestBase):
    pass


@dataclass
class UnitEconomyResult:
    product_cost: int
    pack_cost: int
    marketplace_commission: int
    logistic_price: int
    storage_price: int
    margin: int
    recommended_price: int
    transit_profit: int
    roi: float
    transit_margin: float


@dataclass
class FrequencyResult:
    frequencies: dict[int, int]

    def get_graph_coordinates(self) -> tuple[list[int], list[int]]:
        x, y = [], []
        for key in self.frequencies.keys():
            x.append(key)
            y.append(self.frequencies[key])
        return x, y
