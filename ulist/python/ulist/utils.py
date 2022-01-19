from typing import Callable, Union

import ulist as ul

from .typedef import ELEM, LIST_PY, COUNTER


def check_test_result(
    dtype: str,
    test_method: Union[Callable, str],
    result: Union[ELEM, LIST_PY, ul.UltraFastList],
    expected_value: Union[ELEM, LIST_PY, COUNTER],
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
    if isinstance(result, list) and \
            isinstance(expected_value, list):
        for x, y in zip(result, expected_value):
            assert type(x) == type(y) and x == y, msg
    elif isinstance(result, dict) and \
            isinstance(expected_value, dict):
        for key in result.keys():
            x = result[key]
            y = result[key]
            assert type(x) == type(y) and x == y
        assert len(result) == len(expected_value)
    else:
        assert type(result) == type(expected_value), msg
        assert result == expected_value, msg
