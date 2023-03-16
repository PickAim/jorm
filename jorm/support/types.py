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


class ProductSpecifyDict(AnyJORMDict):
    def __init__(self, mapping: dict | None = None, **kwargs):
        super().__init__(mapping, **kwargs)

    def __setitem__(self, key: str, value: int):
        if not isinstance(key, str) or not isinstance(value, int):
            raise Exception(str(self.__class__.__name__) +
                            ": Not completable arguments type to insert in dict")
        super().__setitem__(key, value)

    def __getitem__(self, item: str) -> int:
        if not isinstance(item, str):
            raise Exception(str(self.__class__.__name__) +
                            ": Not completable arguments type to get item from dict")
        return super().__getitem__(item)

    def get_all_leftovers(self) -> int:
        result: int = 0
        for value in self.values():
            result += value
        return result


class StorageDict(AnyJORMDict):
    def __init__(self, mapping: dict | None = None, **kwargs):
        super().__init__(mapping, **kwargs)

    def __setitem__(self, key: int, value: ProductSpecifyDict):
        if not isinstance(key, int) or not isinstance(value, ProductSpecifyDict):
            raise Exception(str(self.__class__.__name__) +
                            ": Not completable arguments type to insert in dict")
        super().__setitem__(key, value)

    def __getitem__(self, item: int) -> ProductSpecifyDict:
        if not isinstance(item, int):
            raise Exception(str(self.__class__.__name__) +
                            ": Not completable arguments type to get item from dict")
        return super().__getitem__(item)

    def get_all_leftovers(self) -> int:
        result: int = 0
        for value in self.values():
            result += value.get_all_leftovers()
        return result
