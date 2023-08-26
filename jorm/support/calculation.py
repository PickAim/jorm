from dataclasses import dataclass


@dataclass
class UnitEconomyCalculateData:
    buy_price: int
    pack_price: int
    transit_price: int = 0.0
    transit_count: int = 0.0
    market_place_transit_price: int = 0.0


@dataclass
class UnitEconomyCalculateResult:
    product_cost: int  # Закупочная себестоимость
    pack_cost: int  # Упаковка
    marketplace_commission: int  # Комиссия маркетплейса
    logistic_price: int  # Логистика
    storage_price: int  # Хранение
    margin: int  # Маржа в копейках
    recommended_price: int
    transit_profit: int  # Чистая прибыль с транзита
    roi: float  # ROI
    transit_margin: float  # Маржа с транзита (%)


@dataclass
class GreenTradeZoneCalculateResult:
    frequencies: list[int]
    segments: list[tuple[int, int]]
    best_segment_idx: int

    segment_profits: list[int]
    best_segment_profit_idx: int

    mean_segment_profit: list[int]
    best_mean_segment_profit_idx: int

    mean_product_profit: list[int]
    best_mean_product_profit_idx: int

    segment_product_count: list[int]
    best_segment_product_count_idx: int

    segment_product_with_trades_count: list[int]
    best_segment_product_with_trades_count_idx: int


@dataclass
class NicheCharacteristicsCalculateResult:
    card_count: int
    niche_profit: int
    card_trade_count: int
    mean_card_rating: float
    card_with_trades_count: int
    daily_mean_niche_profit: int
    daily_mean_trade_count: int
    mean_traded_card_cost: int
    month_mean_niche_profit_per_card: int
    monopoly_percent: float
    maximum_profit_idx: int
