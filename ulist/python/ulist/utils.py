from collections import abc
from typing import Callable, Union

import ulist as ul

from .typedef import ELEM, LIST_PY


def check_test_result(
    dtype: str,
    test_method: Union[Callable, str],
    result: Union[ELEM, LIST_PY, ul.UltraFastList],
    expected_value: Union[ELEM, LIST_PY],
):
    """Test if the result is as expected. Both value and type.

    Args:
        dtype (str): 'int', 'float' or 'bool'.
        test_method (Union[Callable, str]): A method name or a function.
        result (Union[ELEM, LIST_PY, ul.UltraFastList])
        expected_value (Union[ELEM, LIST_PY])
    """
    msg = (
        f"dtype - {dtype}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    if isinstance(result, ul.UltraFastList):
        result = result.to_list()
    if isinstance(result, abc.Iterable) and \
            isinstance(expected_value, abc.Iterable):
        for x, y in zip(result, expected_value):
            assert type(x) == type(y) and x == y, msg
    else:
        assert type(result) == type(expected_value), msg
        assert result == expected_value, msg
