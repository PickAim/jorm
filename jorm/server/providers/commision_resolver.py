import os
from abc import ABC, abstractmethod

from jorm.market.infrastructure import HandlerType


class CommissionResolver(ABC):
    def __init__(self):
        self._commission_data: dict
        self._warehouse_data: dict


    @abstractmethod
    def _get_commission_for_niche(self, niche_name: str) -> dict[str, float]:
        pass

    @abstractmethod
    def get_commission_for_niche_mapped(self, niche_name: str) -> dict[HandlerType: float]:
        pass

    @abstractmethod
    def get_return_percent_for(self, niche_name: str) -> float:
        pass

    @abstractmethod
    def get_data_for_warehouse(self, warehouse_id: str) -> float:
        pass

