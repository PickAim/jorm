from dataclasses import dataclass
from datetime import datetime

from jorm.support.calculation import SimpleEconomyResult, TransitEconomyResult


@dataclass
class RequestInfo:
    id: int = -1
    date: datetime = datetime.utcnow()
    name: str = ""


class Request:
    pass


@dataclass
class NicheRequest(Request):
    niche_id: int
    category_id: int
    marketplace_id: int


@dataclass
class SimpleEconomyRequest(NicheRequest):
    product_exist_cost: int  # user defined cost for product
    cost_price: int  # how much it cost for user
    length: int
    width: int
    height: int
    mass: int
    target_warehouse_name: str


@dataclass
class TransitEconomyRequest(SimpleEconomyRequest):
    transit_price: int
    transit_count: int


@dataclass
class SaveObject:
    info: RequestInfo


@dataclass
class SimpleEconomySaveObject(SaveObject):
    user_result: tuple[SimpleEconomyRequest, SimpleEconomyResult]
    recommended_result: tuple[SimpleEconomyRequest, SimpleEconomyResult]


@dataclass
class TransitEconomySaveObject(SaveObject):
    user_result: tuple[TransitEconomyRequest, TransitEconomyResult]
    recommended_result: tuple[TransitEconomyRequest, TransitEconomyResult]
