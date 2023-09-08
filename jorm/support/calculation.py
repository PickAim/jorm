from dataclasses import dataclass


class CalculationResult:
    pass


@dataclass
class SimpleEconomyResult(CalculationResult):
    result_cost: int  # recommended or user defined cost
    logistic_price: int
    storage_price: int
    purchase_cost: int  # cost price OR cost price + transit/count
    marketplace_expanses: int
    absolute_margin: int
    relative_margin: float
    roi: float


@dataclass
class TransitEconomyResult(SimpleEconomyResult):
    purchase_investments: int
    commercial_expanses: int
    tax_expanses: int
    absolute_transit_margin: int
    relative_transit_margin: float
    transit_roi: float


@dataclass
class GreenTradeZoneCalculateResult(CalculationResult):
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
class NicheCharacteristicsCalculateResult(CalculationResult):
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
