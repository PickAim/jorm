from dataclasses import dataclass

from jorm.support import keywords


@dataclass
class __UnitEconomyRequestBase:
    buy: int
    pack: int
    niche: str


@dataclass
class __UnitEconomyRequestDefaultBase:
    transit_count: int = 0
    transit_price: int = 0
    market_place_transit_price: int = 0
    warehouse_name: str = keywords.DEFAULT_WAREHOUSE


@dataclass
class __FrequencyRequestBase:
    search_str: str


@dataclass
class __FrequencyRequestDefaultBase:
    pass
