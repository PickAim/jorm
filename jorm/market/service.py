from dataclasses import dataclass
from datetime import datetime


@dataclass
class RequestInfo:
    id: int = -1
    date: datetime = datetime.utcnow()
    name: str = ""


class Request:
    pass


@dataclass
class UnitEconomyRequest(Request):
    buy: int
    pack: int
    niche: str
    category: str
    marketplace_id: int
    transit_count: int = -1
    transit_price: int = -1
    market_place_transit_price: int = -1
    warehouse_name: str = None


@dataclass
class FrequencyRequest(Request):
    niche_name: str
    category_name: str
    marketplace_id: int


class Result:
    pass


@dataclass
class UnitEconomyResult(Result):
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
class FrequencyResult(Result):
    x: list[int]
    y: list[int]
