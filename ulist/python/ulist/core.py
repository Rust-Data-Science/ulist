from .ulist import FloatList, IntegerList, BooleanList
from typing import Iterable, Union

NUM_TYPE = Union[int, float]


class UltraFastList:
    def __init__(self, arr: Iterable[NUM_TYPE], dtype: str) -> None:

        if dtype == "int":
            self._list = IntegerList(arr)
        elif dtype == "float":
            self._list = FloatList(arr)
        else:
            raise ValueError("Parameter dtype should be either 'int' or 'float'!")
