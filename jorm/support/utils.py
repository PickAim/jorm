from typing import TypeVar, Iterable

T = TypeVar("T")


def intersection(it_a: Iterable[T], it_b: Iterable[T]) -> list[T]:
    return [element for element in it_a if element in it_b]
