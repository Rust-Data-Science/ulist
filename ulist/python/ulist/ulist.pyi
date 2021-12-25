from typing import Iterable, List

from .typedef import ELEM, NUM, NUM_LIST_RS


class BooleanList:
    # Arrange the following methods in alphabetical order.

    def __init__(self, vec: Iterable[bool]) -> None: ...
    def all(self) -> bool: ...
    def and_(self, other: BooleanList) -> BooleanList: ...
    def any(self) -> bool: ...
    def append(self, num: ELEM): ...
    def copy(self) -> BooleanList: ...
    def get(self, index: int) -> bool: ...
    def not_(self) -> BooleanList: ...
    def or_(self, other: BooleanList) -> BooleanList: ...
    def pop(self): ...
    def replace(self, old: ELEM, new: ELEM): ...
    def set(self, index: int, num: ELEM): ...
    def size(self) -> int: ...
    def to_list(self) -> List[bool]: ...


class FloatList:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Iterable[float]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> FloatList: ...
    def add_scala(self, num: NUM) -> FloatList: ...
    def append(self, num: ELEM) -> None: ...
    def copy(self) -> FloatList: ...
    def div(self, other: NUM_LIST_RS) -> FloatList: ...
    def div_scala(self, num: float) -> FloatList: ...
    def filter(self, condition: BooleanList) -> FloatList: ...
    def get(self, index: int) -> float: ...
    def greater_than_scala(self, num: NUM) -> BooleanList: ...
    def less_than_scala(self, num: NUM) -> BooleanList: ...
    def max(self) -> float: ...
    def mean(self) -> float: ...
    def min(self) -> float: ...
    def mul(self, other: NUM_LIST_RS) -> FloatList: ...
    def mul_scala(self, num: NUM) -> FloatList: ...
    def pop(self) -> None: ...
    def pow_scala(self, num: int) -> FloatList: ...
    def replace(self, old: ELEM, new: ELEM) -> None: ...
    def set(self, index: int, num: ELEM) -> None: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> FloatList: ...
    def sub(self, other: NUM_LIST_RS) -> FloatList: ...
    def sub_scala(self, num: NUM) -> FloatList: ...
    def sum(self) -> float: ...
    def to_list(self) -> List[float]: ...
    def unique(self) -> FloatList: ...


class IntegerList:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Iterable[int]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> IntegerList: ...
    def add_scala(self, num: NUM) -> IntegerList: ...
    def append(self, num: ELEM) -> None: ...
    def copy(self) -> IntegerList: ...
    def div(self, other: NUM_LIST_RS) -> FloatList: ...
    def div_scala(self, num: float) -> FloatList: ...
    def equal_scala(self, num: int) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> IntegerList: ...
    def get(self, index: int) -> int: ...
    def greater_than_or_equal_scala(self, num: int) -> BooleanList: ...
    def greater_than_scala(self, num: NUM) -> BooleanList: ...
    def less_than_or_equal_scala(self, num: int) -> BooleanList: ...
    def less_than_scala(self, num: NUM) -> BooleanList: ...
    def max(self) -> int: ...
    def mean(self) -> float: ...
    def min(self) -> int: ...
    def mul(self, other: NUM_LIST_RS) -> IntegerList: ...
    def mul_scala(self, num: NUM) -> IntegerList: ...
    def not_equal_scala(self, num: int) -> BooleanList: ...
    def pop(self) -> None: ...
    def pow_scala(self, num: int) -> IntegerList: ...
    def set(self, index: int, num: ELEM) -> None: ...
    def replace(self, old: ELEM, new: ELEM) -> None: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> IntegerList: ...
    def sub(self, other: NUM_LIST_RS) -> IntegerList: ...
    def sub_scala(self, num: NUM) -> IntegerList: ...
    def sum(self) -> int: ...
    def to_list(self) -> List[int]: ...
    def unique(self) -> IntegerList: ...
