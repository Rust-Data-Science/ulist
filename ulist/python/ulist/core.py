from typing import Callable, Iterable

from .typedef import ELEM, LIST_PY, LIST_RS, NUM, NUM_OR_LIST
from .ulist import BooleanList, FloatList, IntegerList


class UltraFastList:
    # Arrange the following methods in alphabetical order.

    def __init__(self, values: LIST_RS) -> None:
        if type(values) is FloatList:
            self.dtype = "float"
        elif type(values) is IntegerList:
            self.dtype = "int"
        elif type(values) is BooleanList:
            self.dtype = "bool"
        else:
            raise TypeError(
                "Parameter values should be FloatList, "
                + "IntegerList or BooleanList type!"
            )
        self._values = values

    def __len__(self) -> int:
        return self.size()

    def _arithmetic_method(
        self, other: NUM_OR_LIST, fn: Callable, fn_scala: Callable
    ) -> "UltraFastList":
        if isinstance(other, int) or isinstance(other, float):
            return fn_scala(other)
        if type(other) is type(self):
            return fn(other)
        raise TypeError(
            "Parameter other should be int, " + "float or UltraFastList type!"
        )

    def __add__(self, other: NUM_OR_LIST) -> "UltraFastList":
        return self._arithmetic_method(other, self.add, self.add_scala)

    def __and__(self, other: "UltraFastList") -> "UltraFastList":
        return self.and_(other)

    def __eq__(self, other: int) -> "UltraFastList":  # type: ignore
        return self.equal_scala(other)

    def __getitem__(self, index: int) -> ELEM:
        return self._values.get(index)

    def __ge__(self, other: int) -> "UltraFastList":
        return self.greater_than_or_equal_scala(other)

    def __gt__(self, other: NUM) -> "UltraFastList":
        return self.greater_than_scala(other)

    def __invert__(self) -> "UltraFastList":
        return self.not_()

    def __le__(self, other: int) -> "UltraFastList":
        return self.less_than_or_equal_scala(other)

    def __lt__(self, other: NUM) -> "UltraFastList":
        return self.less_than_scala(other)

    def __mul__(self, other: NUM_OR_LIST) -> "UltraFastList":
        return self._arithmetic_method(other, self.mul, self.mul_scala)

    def __ne__(self, other: int) -> "UltraFastList":  # type: ignore
        return self.not_equal_scala(other)

    def __or__(self, other: "UltraFastList") -> "UltraFastList":
        return self.or_(other)

    def __pow__(self, other: int) -> "UltraFastList":
        return self._arithmetic_method(other, lambda: None, self.pow_scala)

    def __setitem__(self, index: int, num: ELEM) -> None:
        self._values.set(index, num)

    def __str__(self) -> str:
        n = self.size()
        if n < 100:
            return f"UltraFastList({str(self.to_list())})"
        return (
            f"UltraFastList([{self[0]}, {self[1]}, {self[2]}, ..., "
            + f"{self[n-3]}, {self[n-2]}, {self[n-1]}])"
        )

    def __sub__(self, other: NUM_OR_LIST) -> "UltraFastList":
        return self._arithmetic_method(other, self.sub, self.sub_scala)

    def __truediv__(self, other: NUM_OR_LIST) -> "UltraFastList":
        return self._arithmetic_method(other, self.div, self.div_scala)

    def add(self, other: "UltraFastList") -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        assert not isinstance(other._values, BooleanList)
        return UltraFastList(self._values.add(other._values))

    def add_scala(self, num: NUM) -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        return UltraFastList(self._values.add_scala(num))

    def all(self) -> bool:
        assert isinstance(self._values, BooleanList)
        return self._values.all()

    def and_(self, other: "UltraFastList") -> "UltraFastList":
        assert isinstance(self._values, BooleanList)
        assert isinstance(other._values, BooleanList)
        return UltraFastList(self._values.and_(other._values))

    def any(self) -> bool:
        assert isinstance(self._values, BooleanList)
        return self._values.any()

    def append(self, num: ELEM) -> None:
        self._values.append(num)

    def copy(self) -> "UltraFastList":
        return UltraFastList(self._values.copy())

    def div(self, other: "UltraFastList") -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        assert not isinstance(other._values, BooleanList)
        return UltraFastList(self._values.div(other._values))

    def div_scala(self, num: float) -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        return UltraFastList(self._values.div_scala(num))

    def equal_scala(self, num: int) -> "UltraFastList":
        assert isinstance(self._values, IntegerList)
        return UltraFastList(self._values.equal_scala(num))

    def filter(self, condition: "UltraFastList") -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        assert isinstance(condition._values, BooleanList)
        return UltraFastList(self._values.filter(condition._values))

    def get(self, index: int) -> ELEM:
        return self._values.get(index)

    def greater_than_or_equal_scala(self, num: int) -> "UltraFastList":
        assert isinstance(self._values, IntegerList)
        return UltraFastList(self._values.greater_than_or_equal_scala(num))

    def greater_than_scala(self, num: NUM) -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        return UltraFastList(self._values.greater_than_scala(num))

    def less_than_or_equal_scala(self, num: int) -> "UltraFastList":
        assert isinstance(self._values, IntegerList)
        return UltraFastList(self._values.less_than_or_equal_scala(num))

    def less_than_scala(self, num: NUM) -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        return UltraFastList(self._values.less_than_scala(num))

    def max(self) -> NUM:
        assert not isinstance(self._values, BooleanList)
        return self._values.max()

    def mean(self) -> float:
        assert not isinstance(self._values, BooleanList)
        return self._values.mean()

    def min(self) -> NUM:
        assert not isinstance(self._values, BooleanList)
        return self._values.min()

    def mul(self, other: "UltraFastList") -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        assert not isinstance(other._values, BooleanList)
        return UltraFastList(self._values.mul(other._values))

    def mul_scala(self, num: NUM) -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        return UltraFastList(self._values.mul_scala(num))

    def not_(self) -> "UltraFastList":
        assert isinstance(self._values, BooleanList)
        return UltraFastList(self._values.not_())

    def not_equal_scala(self, num: int) -> "UltraFastList":
        assert isinstance(self._values, IntegerList)
        return UltraFastList(self._values.not_equal_scala(num))

    def or_(self, other: "UltraFastList") -> "UltraFastList":
        assert isinstance(self._values, BooleanList)
        assert isinstance(other._values, BooleanList)
        return UltraFastList(self._values.or_(other._values))

    def pop(self) -> None:
        self._values.pop()

    def pow_scala(self, num: int) -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        return UltraFastList(self._values.pow_scala(num))

    def replace(self, old: ELEM, new: ELEM) -> None:
        self._values.replace(old, new)

    def set(self, index: int, num: ELEM) -> None:
        self._values.set(index, num)

    def size(self) -> int:
        return self._values.size()

    def sort(self, ascending: bool) -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        return UltraFastList(self._values.sort(ascending=ascending))

    def sub(self, other: "UltraFastList") -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        assert not isinstance(other._values, BooleanList)
        return UltraFastList(self._values.sub(other._values))

    def sub_scala(self, num: NUM) -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        return UltraFastList(self._values.sub_scala(num))

    def sum(self) -> NUM:
        assert not isinstance(self._values, BooleanList)
        return self._values.sum()

    def to_list(self) -> LIST_PY:
        return self._values.to_list()

    def unique(self) -> "UltraFastList":
        assert not isinstance(self._values, BooleanList)
        return UltraFastList(self._values.unique())


def from_iter(obj: Iterable, dtype: str) -> "UltraFastList":
    if dtype == "int":
        return UltraFastList(IntegerList(obj))
    elif dtype == "float":
        return UltraFastList(FloatList(obj))
    elif dtype == "bool":
        return UltraFastList(BooleanList(obj))
    else:
        raise ValueError("Parameter dtype should be 'int', 'float' or 'bool'!")
