from collections import abc
from typing import List, Union

import pytest
import ulist as ul

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


@pytest.mark.parametrize(
    "nums, test_method, expected_value, kwargs",
    [
        ([1, 2, 3], "equal_scala", [False, True, False], {"num": 2}),
        ([1, 2, 3], "__eq__", [False, True, False], {"other": 2}),
    ],
)
def test_methods(
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    dtype = "int"
    arr = ul.from_iter(nums, dtype=dtype)
    result = getattr(arr, test_method)(**kwargs)
    if hasattr(result, "to_list"):
        result = result.to_list()
    msg = (
        f"dtype - {dtype}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    if isinstance(result, abc.Iterable):
        for x, y in zip(result, expected_value):
            assert type(x) == type(y) and x == y, msg
    else:
        assert type(result) == type(expected_value), msg
        assert result == expected_value, msg
