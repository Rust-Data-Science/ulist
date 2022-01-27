from typing import Optional, Sequence

from .core import UltraFastList
from .ulist import BooleanList, FloatList, IntegerList, StringList
from .ulist import arange as _arange
from .typedef import ELEM


def arange(start: int, stop: Optional[int] = None, step: int = 1
           ) -> UltraFastList:
    """Return evenly spaced values within a given interval, which is similar
    to the Python built-in range function, but returns an ulist rather than
    a list.

    Args:
        start (int):
            Start of interval. The interval includes this value.
            If stop is not given, then start=0 and stop=start.
        stop (Optional[int], optional):
            End of interval. The interval does not include this value.
            Defaults to None.
        step (int, optional):
            Spacing between values. Defaults to 1.

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


def cycle(obj: Sequence, size: int, dtype: str) -> UltraFastList:
    """Repeats a sequence endlessly until the size is met.

    Args:
        obj (Sequence):
            Sequence object such as list, tuple and range.
        size (int):
            size (int): Size of the new ulist.
        dtype (str):
            The type of the output ulist. 'int', 'float', 'bool' or 'string'.

    Raises:
        ValueError:
            Parameter dtype should be 'int', 'float', 'bool' or 'string'!

    Returns:
        UltraFastList: A ulist object.

    Examples
    --------
    >>> import ulist as ul
    >>> arr1 = ul.cycle(range(3), 5, 'int')
    >>> arr1
    UltraFastList([0, 1, 2, 0, 1])

    >>> arr2 = ul.cycle((0.0, 0.1), 4, 'float')
    >>> arr2
    UltraFastList([0.0, 0.1, 0.0, 0.1])

    >>> arr3 = ul.cycle([True], 3, 'bool')
    >>> arr3
    UltraFastList([True, True, True])

    >>> arr4 = ul.cycle(['foo'], 3, 'string')
    >>> arr4
    UltraFastList(['foo', 'foo', 'foo'])
    """
    if dtype == "int":
        result = UltraFastList(IntegerList.cycle(obj, size))
    elif dtype == "float":
        result = UltraFastList(FloatList.cycle(obj, size))
    elif dtype == "bool":
        result = UltraFastList(BooleanList.cycle(obj, size))
    elif dtype == "string":
        result = UltraFastList(StringList.cycle(obj, size))
    else:
        raise ValueError(
            "Parameter dtype should be 'int', 'float', 'bool' or 'string'!")
    return result


def from_seq(obj: Sequence, dtype: str) -> UltraFastList:
    """Construct a ulist object from a sequence object.

    Args:
        obj (Sequence):
            Sequence object such as list, tuple and range.
        dtype (str):
            The type of the output ulist. 'int', 'float', 'bool' or 'string'.

    Raises:
        ValueError:
            Parameter dtype should be 'int', 'float', 'bool' or 'string'!

    Returns:
        UltraFastList: A ulist object.

    Examples
    --------
    >>> import ulist as ul
    >>> arr1 = ul.from_seq([1.0, 2.0, 3.0], dtype='float')
    >>> arr1
    UltraFastList([1.0, 2.0, 3.0])

    >>> arr2 = ul.from_seq(range(3), dtype='int')
    >>> arr2
    UltraFastList([0, 1, 2])

    >>> arr3 = ul.from_seq((True, True, False), dtype='bool')
    >>> arr3
    UltraFastList([True, True, False])

    >>> arr4 = ul.from_seq(('foo', 'bar', 'baz'), dtype='string')
    >>> arr4
    UltraFastList(['foo', 'bar', 'baz'])
    """
    if dtype == "int":
        result = UltraFastList(IntegerList(obj))
    elif dtype == "float":
        result = UltraFastList(FloatList(obj))
    elif dtype == "bool":
        result = UltraFastList(BooleanList(obj))
    elif dtype == "string":
        result = UltraFastList(StringList(obj))
    else:
        raise ValueError(
            "Parameter dtype should be 'int', 'float', 'bool' or 'string'!")
    return result


def repeat(elem: ELEM, size: int) -> UltraFastList:
    """Return a new ulist of given size, filled with elem.

    Args:
        elem (ELEM): Element to repeat.
        size (int): Size of the new ulist.

    Raises:
        TypeError: Parameter elem should be int, float, bool or str type!

    Returns:
        UltraFastList: A ulist object.

    Examples
    --------
    >>> import ulist as ul
    >>> arr1 = ul.repeat(0, 3)
    >>> arr1
    UltraFastList([0, 0, 0])

    >>> arr2 = ul.repeat(1.0, 3)
    >>> arr2
    UltraFastList([1.0, 1.0, 1.0])

    >>> arr3 = ul.repeat(True, 3)
    >>> arr3
    UltraFastList([True, True, True])

    >>> arr4 = ul.repeat('foo', 3)
    >>> arr4
    UltraFastList(['foo', 'foo', 'foo'])
    """
    if isinstance(elem, bool):
        return UltraFastList(BooleanList.repeat(elem, size))
    elif isinstance(elem, float):
        return UltraFastList(FloatList.repeat(elem, size))
    elif isinstance(elem, int):
        return UltraFastList(IntegerList.repeat(elem, size))
    elif isinstance(elem, str):
        return UltraFastList(StringList.repeat(elem, size))
    else:
        raise TypeError(
            "Parameter elem should be int, float, bool or str type!")
