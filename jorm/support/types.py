from dataclasses import dataclass


class AnyJORMDict(dict):
    def __init__(self, mapping: dict | None = None, **kwargs):
        if mapping is not None:
            mapping = {
                key: value for key, value in mapping.items()
            }
        else:
            mapping = {}
        if kwargs:
            mapping.update(
                {key: value for key, value in kwargs.items()}
            )
        super().__init__(mapping)


@dataclass
class DownturnSumCount:
    sum: int = 0
    count: int = 0


class DownturnMap(dict[str, DownturnSumCount]):
    pass


@dataclass
class SpecifiedLeftover:
    specify: str
    leftover: int

    def __str__(self) -> str:
        return f'{self.specify}: {self.leftover}'

    def __repr__(self) -> str:
        return f'{self.specify}: {self.leftover}'

    def __eq__(self, other):
        return self.specify == other.specify and self.leftover == other.leftover


class StorageDict(dict[int, list[SpecifiedLeftover]]):
    def __init__(self, mapping: dict[int, list[SpecifiedLeftover]] | None = None):
        if mapping is None:
            mapping = {}
        super().__init__(mapping)

    def __setitem__(self, key: int, value: list[SpecifiedLeftover]):
        if not isinstance(key, int) or not isinstance(value, list):
            raise Exception(self.__class__.__name__ +
                            ": Not completable arguments type to insert in dict")
        super().__setitem__(key, value)

    def __getitem__(self, item: int) -> list[SpecifiedLeftover]:
        if not isinstance(item, int):
            raise Exception(self.__class__.__name__ +
                            ": Not completable arguments type to get item from dict")
        return super().__getitem__(item)

    def get_all_leftovers(self) -> int:
        result: int = 0
        for value in self.values():
            result += sum(v.leftover for v in value)
        return result

    def get_mapped_leftovers(self) -> dict[int, dict[str, int]]:
        return {
            key: {
                specified_leftover.specify: specified_leftover.leftover
                for specified_leftover in self.get(key)
            }
            for key in self.keys()
        }


@dataclass
class SpecifiedTopPlaceDict(dict[str, int]):
    def __init__(self, mapping: dict[str, int] | None = None):
        if mapping is None:
            mapping = {}
        super().__init__(mapping)


@dataclass
class EconomyConstants:
    max_mass: float
    max_side_sum: float
    max_side_length: float
    max_standard_volume_in_liters: float
    return_price: int
    oversize_logistic_price: int
    oversize_storage_price: int
    standard_warehouse_logistic_price: int
    standard_warehouse_storage_price: int
    nds_tax: float
    commercial_tax: float
    self_employed_tax: float
