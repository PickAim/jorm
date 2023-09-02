from dataclasses import dataclass


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
