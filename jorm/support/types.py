from typing import Dict


class ProductSpecifyDict(Dict[str, int]):
    def __init__(self):
        super(ProductSpecifyDict, self).__init__()

    def __setitem__(self, key: str, value: int):
        if not isinstance(key, str) or not isinstance(value, int):
            raise Exception(str(self.__class__.__name__) + ": Not completable arguments type to insert in dict")
        super().__setitem__(key, value)

    def get_all_leftovers(self) -> int:
        result: int = 0
        for value in self.values():
            result += value
        return result


class StorageDict(Dict[int, ProductSpecifyDict]):
    def __init__(self):
        super(StorageDict, self).__init__()

    def __setitem__(self, key: int, value: ProductSpecifyDict):
        if not isinstance(key, int) or not isinstance(value, ProductSpecifyDict):
            raise Exception(str(self.__class__.__name__) + ": Not completable arguments type to insert in dict")
        super().__setitem__(key, value)

    def get_all_leftovers(self) -> int:
        result: int = 0
        for value in self.values():
            result += value.get_all_leftovers()
        return result

