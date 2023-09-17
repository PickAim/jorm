import os
from abc import ABC, abstractmethod

from jorm.market.infrastructure import HandlerType


class CommissionResolver(ABC):
    def __init__(self):
        self._commission_data: dict = self.__template_get_commission_data()
        self._warehouse_data: dict = self.__template_get_warehouse_data()

    @abstractmethod
    def update_commission_file(self, filepath: str) -> None:
        pass

    @abstractmethod
    def update_warehouse_file(self, filepath: str) -> None:
        pass

    @abstractmethod
    def get_commision_binary_path(self) -> str:
        pass

    @abstractmethod
    def get_commision_csv_path(self) -> str:
        pass

    @abstractmethod
    def get_warehouse_binary_path(self) -> str:
        pass

    @abstractmethod
    def get_warehouse_file_path(self) -> str:
        pass

    @abstractmethod
    def _get_commission_data(self, binary_path: str) -> dict[str, any]:
        pass

    @abstractmethod
    def _get_warehouse_data(self, binary_path: str) -> dict[str, any]:
        pass

    def __template_get_commission_data(self) -> dict[str, any]:
        binary_path: str = self.get_commision_binary_path()
        if not os.path.exists(binary_path):
            csv_path: str = self.get_commision_csv_path()
            self.update_commission_file(csv_path)
        return self._get_commission_data(binary_path)

    def __template_get_warehouse_data(self) -> dict[str, any]:
        binary_path: str = self.get_warehouse_binary_path()
        if not os.path.exists(binary_path):
            csv_path: str = self.get_warehouse_file_path()
            self.update_warehouse_file(csv_path)
        return self._get_warehouse_data(binary_path)

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
    def get_commision_for_warehouse(self, warehouse_id: str) -> float:
        pass

