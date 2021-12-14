from .ulist import FloatList, IntegerList, BooleanList
from typing import Iterable, Union, List, Callable

NUM_TYPE = Union[int, float]
LIST_TYPE = Union[FloatList, IntegerList, BooleanList]
NUM_OR_LIST_TYPE = Union[NUM_TYPE, "UltraFastList"]


class UltraFastList:
    # Arrange the following methods in alphabetical order.

    def __init__(self, values: LIST_TYPE) -> None:
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
        self, other: NUM_OR_LIST_TYPE, fn: Callable, fn_scala: Callable
    ) -> "UltraFastList":
        if isinstance(other, int) or isinstance(other, float):
            return fn_scala(other)
        if type(other) is type(self):
            return fn(other)
        raise TypeError(
            "Parameter other should be int, " + "float or UltraFastList type!"
        )

    def __add__(self, other: NUM_OR_LIST_TYPE) -> "UltraFastList":
        return self._arithmetic_method(other, self.add, self.add_scala)

    def __eq__(self, other: int) -> "UltraFastList":
        return self.equal_scala(other)

    def __getitem__(self, index: int) -> NUM_TYPE:
        return self._values.get(index)

    def __ge__(self, other: int) -> "UltraFastList":
        return self.greater_than_or_equal_scala(other)

    def __gt__(self, other: NUM_TYPE) -> "UltraFastList":
        return self.greater_than_scala(other)

    def __le__(self, other: NUM_TYPE) -> "UltraFastList":
        return self.less_than_or_equal_scala(other)

    def __lt__(self, other: NUM_TYPE) -> "UltraFastList":
        return self.less_than_scala(other)

    def __mul__(self, other: NUM_OR_LIST_TYPE) -> "UltraFastList":
        return self._arithmetic_method(other, self.mul, self.mul_scala)

    def __ne__(self, other: int) -> "UltraFastList":
        return self.not_equal_scala(other)

    def __pow__(self, other: int) -> "UltraFastList":
        return self._arithmetic_method(other, lambda: None, self.pow_scala)

    def __str__(self) -> str:
        n = self.size()
        if n < 100:
            return f"UltraFastList({str(self.to_list())})"
        return (
            f"UltraFastList([{self[0]}, {self[1]}, {self[2]}, ..., "
            + f"{self[n-3]}, {self[n-2]}, {self[n-1]}])"
        )

    def __sub__(self, other: NUM_OR_LIST_TYPE) -> "UltraFastList":
        return self._arithmetic_method(other, self.sub, self.sub_scala)

    def __truediv__(self, other: NUM_OR_LIST_TYPE) -> "UltraFastList":
        return self._arithmetic_method(other, self.div, self.div_scala)

    def add(self, other: "UltraFastList") -> "UltraFastList":
        return UltraFastList(self._values.add(other._values))

    def add_scala(self, num: NUM_TYPE) -> "UltraFastList":
        return UltraFastList(self._values.add_scala(num))

    def all(self) -> bool:
        return self._values.all()

    def any(self) -> bool:
        return self._values.any()

    def copy(self) -> "UltraFastList":
        return UltraFastList(self._values.copy())

    def div(self, other: "UltraFastList") -> "UltraFastList":
        return UltraFastList(self._values.div(other._values))

    def div_scala(self, num: float) -> "UltraFastList":
        return UltraFastList(self._values.div_scala(num))

    def equal_scala(self, num: int) -> "UltraFastList":
        return UltraFastList(self._values.equal_scala(num))

    def filter(self, condition: "UltraFastList") -> "UltraFastList":
        return UltraFastList(self._values.filter(condition._values))

    def get(self, index: int) -> NUM_TYPE:
        return self._values.get(index)

    def greater_than_or_equal_scala(self, num: int) -> "UltraFastList":
        return UltraFastList(self._values.greater_than_or_equal_scala(num))

    def greater_than_scala(self, num: NUM_TYPE) -> "UltraFastList":
        return UltraFastList(self._values.greater_than_scala(num))

    def less_than_or_equal_scala(self, num: int) -> "UltraFastList":
        return UltraFastList(self._values.less_than_or_equal_scala(num))

    def less_than_scala(self, num: NUM_TYPE) -> "UltraFastList":
        return UltraFastList(self._values.less_than_scala(num))

    def max(self) -> NUM_TYPE:
        return self._values.max()

    def mean(self) -> float:
        return self._values.mean()

    def min(self) -> NUM_TYPE:
        return self._values.min()

    def mul(self, other: "UltraFastList") -> "UltraFastList":
        return UltraFastList(self._values.mul(other._values))

    def mul_scala(self, num: NUM_TYPE) -> "UltraFastList":
        return UltraFastList(self._values.mul_scala(num))

    def not_equal_scala(self, num: int) -> "UltraFastList":
        return UltraFastList(self._values.not_equal_scala(num))

    def pow_scala(self, num: int) -> "UltraFastList":
        return UltraFastList(self._values.pow_scala(num))

    def size(self) -> int:
        return self._values.size()

    def sort(self, ascending: bool) -> "UltraFastList":
        return UltraFastList(self._values.sort(ascending=ascending))

    def sub(self, other: "UltraFastList") -> "UltraFastList":
        return UltraFastList(self._values.sub(other._values))

    def sub_scala(self, num: NUM_TYPE) -> "UltraFastList":
        return UltraFastList(self._values.sub_scala(num))

    def sum(self) -> NUM_TYPE:
        return self._values.sum()

    def to_list(self) -> List[NUM_TYPE]:
        return self._values.to_list()

    def unique(self) -> "UltraFastList":
        return UltraFastList(self._values.unique())


def from_iter(obj: Iterable[NUM_TYPE], dtype: str) -> "UltraFastList":
    if dtype == "int":
        values = IntegerList(obj)
    elif dtype == "float":
        values = FloatList(obj)
    elif dtype == "bool":
        values = BooleanList(obj)
    else:
        raise ValueError("Parameter dtype should be 'int', 'float' or 'bool'!")
    return UltraFastList(values)
