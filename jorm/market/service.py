from dataclasses import dataclass
from datetime import datetime

from jorm.support import keywords


@dataclass
class RequestInfo:
    id: int = -1
    date: datetime = datetime.utcnow()
    name: str = ""


@dataclass
class UnitEconomyRequest:
    buy: int
    pack: int
    niche: str
    transit_count: int = -1
    transit_price: int = -1
    market_place_transit_price: int = -1
    warehouse_name: str = keywords.DEFAULT_WAREHOUSE


@dataclass
class FrequencyRequest:
    search_str: str


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
