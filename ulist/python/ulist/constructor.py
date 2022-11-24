from typing import Optional, Sequence, Union, Type

from .core import UltraFastList
from .typedef import ELEM
from .ulist import (BooleanList, FloatList32, FloatList64, IntegerList32,
                    IntegerList64, StringList, arange32, arange64)

T = Union[
    Type[BooleanList],
    Type[FloatList32],
    Type[FloatList64],
    Type[IntegerList32],
    Type[IntegerList64],
    Type[StringList],
]


def arange(
    start: int,
    stop: Optional[int] = None,
    step: int = 1,
    dtype: str = 'int',
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
        dtype (str, optional):
            The type of the output ulist. 'int', 'int32', 'int64'.

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
    if dtype == "int" or dtype == "int64":
        return UltraFastList(arange64(start=start, stop=stop, step=step))
    elif dtype == "int32":
        return UltraFastList(arange32(start=start, stop=stop, step=step))
    else:
        raise ValueError(
            "Parameter dtype should be 'int', 'int32' or 'int64'!")


def choices(obj: Sequence, size: int, dtype: str) -> UltraFastList:
    """Choose element from a sequence randomly and endlessly until
    the size is met.

    Args:
        obj (Sequence):
            Sequence object such as list, tuple and range.
        size (int):
            size (int): Size of the new ulist.
        dtype (str):
            The type of the output ulist. 'int', 'int32', 'int64',
            'float', 'float32', 'float64', 'bool' or 'string'.

    Raises:
        ValueError:
            Parameter dtype should be 'int', 'int32', 'int64',
            'float', 'float32', 'float64', 'bool' or 'string'!

    Returns:
        UltraFastList: A ulist object.
    """
    if dtype == "int" or dtype == "int64":
        result = UltraFastList(IntegerList64.choices(obj, size))
    elif dtype == "int32":
        result = UltraFastList(IntegerList32.choices(obj, size))
    elif dtype == "float" or dtype == "float64":
        result = UltraFastList(FloatList64.choices(obj, size))
    elif dtype == "float32":
        result = UltraFastList(FloatList32.choices(obj, size))
    elif dtype == "bool":
        result = UltraFastList(BooleanList.choices(obj, size))
    elif dtype == "string":
        result = UltraFastList(StringList.choices(obj, size))
    else:
        raise ValueError(
            "Parameter dtype should be 'int', 'int32', 'int64', " +
            "'float', 'float32', 'float64', 'bool' or 'string'!"
        )
    return result


def cycle(obj: Sequence, size: int, dtype: str) -> UltraFastList:
    """Repeats a sequence endlessly until the size is met.

    Args:
        obj (Sequence):
            Sequence object such as list, tuple and range.
        size (int):
            size (int): Size of the new ulist.
        dtype (str):
            The type of the output ulist. 'int', 'int32', 'int64',
            'float', 'float32', 'float64', 'bool' or 'string'.

    Raises:
        ValueError:
            Parameter dtype should be 'int', 'int32', 'int64',
            'float', 'float32', 'float64', 'bool' or 'string'!

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
    if dtype == "int" or dtype == "int64":
        result = UltraFastList(IntegerList64.cycle(obj, size))
    elif dtype == "int32":
        result = UltraFastList(IntegerList32.cycle(obj, size))
    elif dtype == "float" or dtype == "float64":
        result = UltraFastList(FloatList64.cycle(obj, size))
    elif dtype == "float32":
        result = UltraFastList(FloatList32.cycle(obj, size))
    elif dtype == "bool":
        result = UltraFastList(BooleanList.cycle(obj, size))
    elif dtype == "string":
        result = UltraFastList(StringList.cycle(obj, size))
    else:
        raise ValueError(
            "Parameter dtype should be 'int', 'int32', 'int64', " +
            "'float', 'float32', 'float64', 'bool' or 'string'!"
        )
    return result


def from_seq(obj: Sequence, dtype: str) -> UltraFastList:
    """Construct a ulist object from a sequence object.

    Args:
        obj (Sequence):
            Sequence object such as list, tuple and range.
        dtype (str):
            The type of the output ulist. 'int', 'int32', 'int64',
            'float', 'float32', 'float64', 'bool' or 'string'.

    Raises:
        ValueError:
            Parameter dtype should be 'int', 'int32', 'int64',
            'float', 'float32', 'float64', 'bool' or 'string'!

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
    na_indexes = set([i for i, x in enumerate(obj) if x is None])
    if dtype == "int" or dtype == "int64":
        cls: T = IntegerList64
        na_val: ELEM = 0
    elif dtype == "int32":
        cls = IntegerList32
        na_val = 0
    elif dtype == "float" or dtype == "float64":
        cls = FloatList64
        na_val = 0.0
    elif dtype == "float32":
        cls = FloatList32
        na_val = 0.0
    elif dtype == "bool":
        cls = BooleanList
        na_val = False
    elif dtype == "string":
        cls = StringList
        na_val = ''
    else:
        raise ValueError(
            "Parameter dtype should be 'int', 'int32', 'int64', " +
            "'float', 'float32', 'float64', 'bool' or 'string'!"
        )
    elements = [x if x is not None else na_val for x in obj]
    result = UltraFastList(cls(elements, na_indexes))
    return result


def random(size: int, dtype: str) -> UltraFastList:
    """Return a new ulist of random number in [0.0, 1.0).

    Args:
        size (int):
            size (int): Size of the new ulist.
        dtype (str):
            The type of the output ulist. 'float', 'float32' or 'float64'.
    """
    if dtype == "float" or dtype == "float64":
        result = UltraFastList(FloatList64.random(size))
    elif dtype == "float32":
        result = UltraFastList(FloatList32.random(size))
    else:
        raise ValueError(
            "Parameter dtype should be 'float', 'float32' or 'float64'!"
        )
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
        return UltraFastList(FloatList64.repeat(elem, size))
    elif isinstance(elem, int):
        return UltraFastList(IntegerList64.repeat(elem, size))
    elif isinstance(elem, str):
        return UltraFastList(StringList.repeat(elem, size))
    else:
        raise TypeError(
            "Parameter elem should be int, float, bool or str type!")
