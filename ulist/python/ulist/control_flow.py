from typing import Callable, List

from .core import BooleanList, UltraFastList
from .typedef import ELEM, LIST_PY
from .ulist import select_bool as _select_bool
from .ulist import select_float as _select_float
from .ulist import select_int as _select_int


def select(
        conditions: List[UltraFastList],
        choices: LIST_PY,
        default: ELEM,
) -> UltraFastList:
    """Return a ulist drawn from elements in `choices`, depending on`conditions`.

    Args:
        conditions (List[UltraFastList]):
            The list of conditions which determine from which array in
            `choices` the output elements are taken. When multiple conditions
            are satisfied, the first one encountered in `conditions` is used.
        choices (LIST_PY):
            The list of ulist from which the output elements are taken.
            It has to be of the same length as `conditions`.
        default (ELEM):
            The element inserted in output when all conditions evaluate
            to False.

    Raises:
        TypeError:
            The type of parameter `default` should be bool, float or int!

    Returns:
        UltraFastList: A ulist object.

    Examples
    --------
    >>> import ulist as ul
    >>> arr = ul.arange(6)
    >>> arr
    UltraFastList([0, 1, 2, 3, 4, 5])

    >>> conditions = [arr < 2, arr < 4]
    >>> conditions
    [
        UltraFastList([True, True, False, False, False, False]),
        UltraFastList([True, True, True, True, False, False])
    ]

    >>> result = ul.select(conditions, choices=[0, 1], default=2)
    >>> result
    UltraFastList([0, 0, 1, 1, 2, 2])
    """
    assert len(conditions) == len(choices)

    if type(default) is bool:
        fn: Callable = _select_bool
    elif type(default) is float:
        fn = _select_float
    elif type(default) is int:
        fn = _select_int
    else:
        raise TypeError(
            "The type of parameter `default` should be bool, float or int!"
        )

    _conditions = []
    for cond in conditions:
        assert isinstance(cond._values, BooleanList)
        _conditions.append(cond._values)
    result = fn(_conditions, choices, default)
    return UltraFastList(result)
