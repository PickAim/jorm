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


class SpecMap(dict[str, DownturnSumCount]):
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
        return self.specify == other.specify


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


@dataclass
class SpecifiedTopPlace:
    search_request: str
    place: int

    def __str__(self) -> str:
        return f'{self.search_request}: {self.place}'

    def __repr__(self) -> str:
        return f'{self.search_request}: {self.place}'
