from typing import Iterable
from .core import UltraFastList
from .ulist import BooleanList, FloatList, IntegerList


def from_iter(obj: Iterable, dtype: str) -> UltraFastList:
    """Construct a ulist object from iterable object.

    Args:
        obj (Iterable): Iterable object such as list, set and range.
        dtype (str): 'int', 'float' or 'bool'.

    Returns:
        UltraFastList: A ulist object.
    """
    if dtype == "int":
        return UltraFastList(IntegerList(obj))
    elif dtype == "float":
        return UltraFastList(FloatList(obj))
    elif dtype == "bool":
        return UltraFastList(BooleanList(obj))
    else:
        raise ValueError("Parameter dtype should be 'int', 'float' or 'bool'!")
