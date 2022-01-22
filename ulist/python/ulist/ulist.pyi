from typing import List, Sequence, Dict

from .typedef import ELEM, LIST_PY, NUM, NUM_LIST_RS, LIST_RS


class BooleanList:
    # Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[bool]) -> None: ...
    def all(self) -> bool: ...
    def and_(self, other: BooleanList) -> BooleanList: ...
    def any(self) -> bool: ...
    def append(self, num: ELEM): ...
    def as_float(self) -> FloatList: ...
    def as_int(self) -> IntegerList: ...
    def copy(self) -> BooleanList: ...
    def counter(self) -> Dict[bool, int]: ...
    @staticmethod
    def cycle(obj: Sequence[bool], size: int) -> BooleanList: ...
    def get(self, index: int) -> bool: ...
    def not_(self) -> BooleanList: ...
    def or_(self, other: BooleanList) -> BooleanList: ...
    def pop(self): ...
    @staticmethod
    def repeat(num: bool, size: int) -> BooleanList: ...
    def set(self, index: int, num: ELEM): ...
    def size(self) -> int: ...
    def sum(self) -> int: ...
    def to_list(self) -> List[bool]: ...
    def union(self, other: LIST_RS) -> LIST_RS: ...


class FloatList:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[float]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> FloatList: ...
    def add_scala(self, num: NUM) -> FloatList: ...
    def append(self, num: ELEM) -> None: ...
    def argmax(self) -> int: ...
    def argmin(self) -> int: ...
    def as_bool(self) -> BooleanList: ...
    def as_int(self) -> IntegerList: ...
    def copy(self) -> FloatList: ...
    @staticmethod
    def cycle(obj: Sequence[float], size: int) -> FloatList: ...
    def div(self, other: NUM_LIST_RS) -> FloatList: ...
    def div_scala(self, num: float) -> FloatList: ...
    def equal_scala(self, num: NUM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> FloatList: ...
    def get(self, index: int) -> float: ...
    def greater_than_or_equal_scala(self, num: NUM) -> BooleanList: ...
    def greater_than_scala(self, num: NUM) -> BooleanList: ...
    def less_than_or_equal_scala(self, num: NUM) -> BooleanList: ...
    def less_than_scala(self, num: NUM) -> BooleanList: ...
    def max(self) -> float: ...
    def min(self) -> float: ...
    def mul(self, other: NUM_LIST_RS) -> FloatList: ...
    def mul_scala(self, num: NUM) -> FloatList: ...
    def not_equal_scala(self, num: NUM) -> BooleanList: ...
    def pop(self) -> None: ...
    def pow_scala(self, num: int) -> FloatList: ...
    @staticmethod
    def repeat(num: float, size: int) -> FloatList: ...
    def replace(self, old: ELEM, new: ELEM) -> FloatList: ...
    def set(self, index: int, num: ELEM) -> None: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> FloatList: ...
    def sub(self, other: NUM_LIST_RS) -> FloatList: ...
    def sub_scala(self, num: NUM) -> FloatList: ...
    def sum(self) -> float: ...
    def to_list(self) -> List[float]: ...
    def union(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> FloatList: ...


class IntegerList:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[int]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> IntegerList: ...
    def add_scala(self, num: NUM) -> IntegerList: ...
    def append(self, num: ELEM) -> None: ...
    def argmax(self) -> int: ...
    def argmin(self) -> int: ...
    def as_bool(self) -> BooleanList: ...
    def as_float(self) -> FloatList: ...
    def copy(self) -> IntegerList: ...
    def counter(self) -> Dict[int, int]: ...
    @staticmethod
    def cycle(obj: Sequence[int], size: int) -> IntegerList: ...
    def div(self, other: NUM_LIST_RS) -> FloatList: ...
    def div_scala(self, num: float) -> FloatList: ...
    def equal_scala(self, num: NUM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> IntegerList: ...
    def get(self, index: int) -> int: ...
    def greater_than_or_equal_scala(self, num: NUM) -> BooleanList: ...
    def greater_than_scala(self, num: NUM) -> BooleanList: ...
    def less_than_or_equal_scala(self, num: NUM) -> BooleanList: ...
    def less_than_scala(self, num: NUM) -> BooleanList: ...
    def max(self) -> int: ...
    def min(self) -> int: ...
    def mul(self, other: NUM_LIST_RS) -> IntegerList: ...
    def mul_scala(self, num: NUM) -> IntegerList: ...
    def not_equal_scala(self, num: NUM) -> BooleanList: ...
    def pop(self) -> None: ...
    def pow_scala(self, num: int) -> IntegerList: ...
    def set(self, index: int, num: ELEM) -> None: ...
    @staticmethod
    def repeat(num: int, size: int) -> IntegerList: ...
    def replace(self, old: ELEM, new: ELEM) -> IntegerList: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> IntegerList: ...
    def sub(self, other: NUM_LIST_RS) -> IntegerList: ...
    def sub_scala(self, num: NUM) -> IntegerList: ...
    def sum(self) -> int: ...
    def to_list(self) -> List[int]: ...
    def union(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> IntegerList: ...


def arange(start: int, stop: int, step: int) -> IntegerList: ...


def select_bool(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: bool,
) -> BooleanList: ...


def select_float(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: float,
) -> FloatList: ...


def select_int(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: int,
) -> IntegerList: ...
