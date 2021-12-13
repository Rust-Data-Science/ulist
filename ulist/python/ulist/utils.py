from collections import abc
from typing import List, Union


import ulist as ul

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


def check_test_result(
    dtype: str,
    test_method: str,
    result: Union[NUM_TYPE, LIST_TYPE, ul.UltraFastList],
    expected_value: LIST_TYPE,
):
    msg = (
        f"dtype - {dtype}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    if hasattr(result, "to_list"):
        result = result.to_list()
    if isinstance(result, abc.Iterable):
        for x, y in zip(result, expected_value):
            assert type(x) == type(y) and x == y, msg
    else:
        assert type(result) == type(expected_value), msg
        assert result == expected_value, msg
