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

    Examples
    --------
    >>> import ulist as ul
    >>> arr1 = ul.from_iter([1.0, 2.0, 3.0], dtype='float')
    >>> arr1
    UltraFastList([1.0, 2.0, 3.0])

    >>> arr2 = ul.from_iter(range(3), dtype='int')
    >>> arr2
    UltraFastList([0, 1, 2])

    >>> arr3 = ul.from_iter(range(3), dtype='int')
    >>> arr2
    UltraFastList([0, 1, 2])

    >>> arr3 = ul.from_iter((True, True, False), dtype='bool')
    >>> arr3
    UltraFastList([True, True, False])
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

    Examples
    --------
    >>> import ulist as ul
    >>> arr1 = ul.arange(3)
    >>> arr1
    UltraFastList([0, 1, 2])

    >>> arr2 = ul.arange(1, 4)
    >>> arr2
    UltraFastList([1, 2, 3])

    >>> arr3 = ul.arange(1, 6, 2)
    >>> arr3
    UltraFastList([1, 3, 5])
    """
    if stop is None:
        stop = start
        start = 0
    return UltraFastList(_arange(start=start, stop=stop, step=step))
