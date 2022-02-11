from __future__ import annotations  # To avoid circular import.
from typing import Callable, List, TYPE_CHECKING

from .ulist import BooleanList
from .typedef import ELEM, LIST_PY
from .ulist import select_bool as _select_bool
from .ulist import select_float as _select_float
from .ulist import select_int as _select_int
from .ulist import select_string as _select_string


if TYPE_CHECKING:  # To avoid circular import.
    from . import UltraFastList


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
            The type of parameter `default` should be bool, float, int or str!

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
    elif type(default) is str:
        fn = _select_string
    else:
        raise TypeError(
            "The type of parameter `default` should be" +
            " bool, float, int or str!"
        )

    _conditions = []
    for cond in conditions:
        assert isinstance(cond._values, BooleanList)
        _conditions.append(cond._values)
    result = fn(_conditions, choices, default)

    from . import UltraFastList  # To avoid circular import.
    return UltraFastList(result)


class CaseObject:
    """
    This is designed to implement `case` method for UtraFastList.
    To provide an interface similar to SQL's `case` statement.
    """

    def __init__(self, nums: UltraFastList, default: ELEM) -> None:
        self._values = nums
        self._default = default
        self._conditions: List[UltraFastList] = []
        self._choices: list = []

    def when(
        self,
        fn: Callable[[UltraFastList], UltraFastList],
        then: ELEM
    ) -> 'CaseObject':
        """Calculate the condition, and keep the condition and element to use.

        Args:
            fn (Callable[[UltraFastList], UltraFastList]):
                Function to calculate the condition.
            then (ELEM):
                The element to use when the condition is satisfied.

        Raises:
            TypeError:
                Calling parameter `fn` should return a ulist with dtype bool!
            TypeError:
                The type of parameter `then` should be the same as `default`!

        Returns:
            CaseObject
        """
        cond = fn(self._values)
        if cond.dtype != "bool":
            raise TypeError(
                "Calling parameter `fn` should return a ulist with dtype bool!"
            )
        self._conditions.append(cond)

        if not isinstance(then, type(self._default)):
            raise TypeError(
                "The type of parameter `then` should be the same as `default`!"
            )
        self._choices.append(then)

        return self

    def end(self) -> UltraFastList:
        """Execute the case statement."""
        return select(self._conditions, self._choices, self._default)
