from .ulist import FloatList, IntegerList, BooleanList
from typing import Iterable, Union, List, Callable

NUM_TYPE = Union[int, float]
LIST_TYPE = Union[FloatList, IntegerList, BooleanList]
NUM_OR_LIST_TYPE = Union[NUM_TYPE, "UltraFastList"]


class UltraFastList:
    def __init__(self, values: LIST_TYPE) -> None:
        if type(values) is FloatList:
            self.dtype = "float"
        elif type(values) is IntegerList:
            self.dtype = "int"
        elif type(values) is BooleanList:
            self.dtype = "bool"
        else:
            raise TypeError(
                "Parameter values should be FloatList, IntegerList or BooleanList type!"
            )
        self._values = values

    def __len__(self) -> int:
        return self.size()

    def _arithmetic_method(
        self,
        other: NUM_OR_LIST_TYPE,
        fn: Callable,
        fn_scala: Callable
    ) -> NUM_OR_LIST_TYPE:
        if isinstance(other, int) or isinstance(other, float):
            return fn_scala(other)
        if type(other) is type(self):
            return fn(other)
        raise TypeError(
            "Parameter other should be int, float or UltraFastList type!"
        )

    def __add__(self, other: NUM_OR_LIST_TYPE) -> NUM_OR_LIST_TYPE:
        return self._arithmetic_method(other, self.add, self.add_scala)

    def __sub__(self, other: NUM_OR_LIST_TYPE) -> NUM_OR_LIST_TYPE:
        return self._arithmetic_method(other, self.sub, self.sub_scala)

    def __mul__(self, other: NUM_OR_LIST_TYPE) -> NUM_OR_LIST_TYPE:
        return self._arithmetic_method(other, self.mul, self.mul_scala)

    def __div__(self, other: NUM_OR_LIST_TYPE) -> NUM_OR_LIST_TYPE:
        return self._arithmetic_method(other, self.div, self.div_scala)

    def add(self, other: "UltraFastList") -> "UltraFastList":
        return UltraFastList(self._values.add(other._values))

    def add_scala(self, num: NUM_TYPE) -> "UltraFastList":
        return UltraFastList(self._values.add_scala(num))

    def copy(self) -> "UltraFastList":
        return UltraFastList(self._values.copy())

    def div(self, other: "UltraFastList") -> "UltraFastList":
        return UltraFastList(self._values.div(other._values))

    def div_scala(self, num: float) -> "UltraFastList":
        return UltraFastList(self._values.div_scala(num))

    def filter(self, condition: "UltraFastList") -> "UltraFastList":
        return UltraFastList(self._values.filter(condition._values))

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
