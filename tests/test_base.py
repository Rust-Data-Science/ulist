from collections import abc
from typing import List, Union

import pytest
import ulist as ul

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


@pytest.mark.parametrize(
    "dtype, nums, test_method, expected_value",
    [
        ("float", [1.0, 2.0], "copy", [1.0, 2.0]),
        ("float", [1.0, 2.0], "size", 2),
        ("float", [1.0, 2.0], "to_list", [1.0, 2.0]),
        ("float", [1.0, 2.0], "__str__", "UltraFastList([1.0, 2.0])"),
        (
            "float",
            range(100),
            "__str__",
            "UltraFastList([0.0, 1.0, 2.0, ..., 97.0, 98.0, 99.0])",
        ),
        ("int", [1, 2], "copy", [1, 2]),
        ("int", [1, 2], "size", 2),
        ("int", [1, 2], "to_list", [1, 2]),
        ("int", [1, 2], "__str__", "UltraFastList([1, 2])"),
        (
            "int",
            range(100),
            "__str__",
            "UltraFastList([0, 1, 2, ..., 97, 98, 99])",
        ),
        ("bool", [True, False], "copy", [True, False]),
        ("bool", [True, False], "size", 2),
        ("bool", [True, False], "to_list", [True, False]),
        ("bool", [True, False], "to_list", [True, False]),
        ("bool", [True, False], "__str__", "UltraFastList([True, False])"),
        (
            "bool",
            [True, False] * 50,
            "__str__",
            "UltraFastList([True, False, True, ..., False, True, False])",
        ),
    ],
)
def test_methods_no_arg(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
):
    arr = ul.from_iter(nums, dtype)
    result = getattr(arr, test_method)()
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


@pytest.mark.parametrize(
    "dtype, nums, test_method, expected_value, kwargs",
    [
        ("float", [1.0, 2.0, 3.0], "__getitem__", 2.0, {"index": 1}),
        ("float", [1.0, 2.0, 3.0], "get", 2.0, {"index": 1}),
        ("int", [1, 2, 3], "__getitem__", 1, {"index": 0}),
        ("int", [1, 2, 3], "get", 1, {"index": 0}),
        ("bool", [True, False, True], "__getitem__", True, {"index": 2}),
        ("bool", [True, False, True], "get", True, {"index": 2}),
    ],
)
def test_methods_with_args(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    arr = ul.from_iter(nums, dtype)
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
