from typing import Iterable, Optional
from .core import UltraFastList
from .ulist import BooleanList, FloatList, IntegerList, arange as _arange


def from_iter(obj: Iterable, dtype: str) -> UltraFastList:
    """Construct a ulist object from an iterable object.

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


def arange(start: int, stop: Optional[int] = None, step: int = 1) -> UltraFastList:
    """Return evenly spaced values within a given interval, which is equivalent to
    the Python built-in range function, but returns an ulist rather than a list.

    Args:
        start (int): [description]
        stop (Optional[int], optional): [description]. Defaults to None.
        step (int, optional): [description]. Defaults to 1.

    Returns:
        UltraFastList: A ulist object.
    """
    if stop is None:
        stop = start
        start = 0
    return UltraFastList(_arange(start=start, stop=stop, step=step))
