# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-11-14 16:02:00
"""
import pytest
import ulist as ul
from typing import Union, List, Optional

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


@pytest.mark.parametrize(
    "dtype, nums",
    [("float", [1.0, 2.0, 3.0, 4.0, 5.0]), ("int", [1, 2, 3, 4, 5])],
)
@pytest.mark.parametrize(
    "test_method, expected_value, expected_type",
    [
        ("max", 5.0, None),
        ("mean", 3.0, float),
        ("min", 1.0, None),
        ("size", 5, int),
        ("sum", 15.0, None),
    ],
)
def test_statistics_methods(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: NUM_TYPE,
    expected_type: Optional[NUM_TYPE],
) -> None:
    arr = ul.from_iter(nums, dtype)
    result = getattr(arr, test_method)()
    msg = (
        f"dtype - {dtype}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    assert result == expected_value, msg

    if expected_type is None:
        if dtype is "float":
            expected_type = float
        elif dtype is "int":
            expected_type = int
    assert type(result) == expected_type, msg

    assert len(arr) == arr.size()


@pytest.mark.parametrize(
    "dtype, nums",
    [("float", [5.0, 3.0, 2.0, 4.0, 1.0, 3.0]), ("int", [5, 3, 2, 4, 1, 3])],
)
@pytest.mark.parametrize(
    "test_method, expected_value, kwargs",
    [
        ("copy", [5, 3, 2, 4, 1, 3], {}),
        (
            "filter",
            [5, 4],
            {
                "condition": ul.from_iter(
                    [True, False, False, True, False, False], "bool"
                )
            },
        ),
        ("sort", [1, 2, 3, 3, 4, 5], {"ascending": True}),
        ("sort", [5, 4, 3, 3, 2, 1], {"ascending": False}),
        ("to_list", [5, 3, 2, 4, 1, 3], {}),
        ("unique", [1, 2, 3, 4, 5], {}),
    ],
)
def test_data_process_methods(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    arr = ul.from_iter(nums, dtype)
    result = getattr(arr, test_method)(**kwargs)
    if test_method != "to_list":
        result = result.to_list()
    msg = (
        f"dtype - {dtype}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    assert result == expected_value, msg


@pytest.mark.parametrize(
    "dtype, nums",
    [("float", [1.0, 2.0, 3.0, 4.0, 5.0]), ("int", [1, 2, 3, 4, 5])],
)
@pytest.mark.parametrize(
    "test_method, expected_value, kwargs",
    [
        ("add", [2, 4, 6, 8, 10], {"other": [1, 2, 3, 4, 5]}),
        ("sub", [0, 0, 0, 0, 0], {"other": [1, 2, 3, 4, 5]}),
        ("mul", [1, 4, 9, 16, 25], {"other": [1, 2, 3, 4, 5]}),
        ("div", [1, 1, 1, 1, 1], {"other": [1, 2, 3, 4, 5]}),
        ("add_scala", [2, 3, 4, 5, 6], {"num": 1}),
        ("sub_scala", [0, 1, 2, 3, 4], {"num": 1}),
        ("mul_scala", [2, 4, 6, 8, 10], {"num": 2}),
        ("div_scala", [0.5, 1.0, 1.5, 2.0, 2.5], {"num": 2}),
        ("pow_scala", [1, 4, 9, 16, 25], {"num": 2}),
        ("__add__", [2, 4, 6, 8, 10], {"other": [1, 2, 3, 4, 5]}),
        ("__sub__", [0, 0, 0, 0, 0], {"other": [1, 2, 3, 4, 5]}),
        ("__mul__", [1, 4, 9, 16, 25], {"other": [1, 2, 3, 4, 5]}),
        ("__truediv__", [1, 1, 1, 1, 1], {"other": [1, 2, 3, 4, 5]}),
        ("__add__", [2, 3, 4, 5, 6], {"other": 1}),
        ("__sub__", [0, 1, 2, 3, 4], {"other": 1}),
        ("__mul__", [2, 4, 6, 8, 10], {"other": 2}),
        ("__truediv__", [0.5, 1.0, 1.5, 2.0, 2.5], {"other": 2}),
    ],
)
def test_arithmetic_methods(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    arr = ul.from_iter(nums, dtype)
    if not test_method.endswith("_scala"):
        if isinstance(kwargs["other"], list):
            result = getattr(arr, test_method)(ul.from_iter(kwargs["other"], dtype))
        else:
            result = getattr(arr, test_method)(kwargs["other"])
    else:
        result = getattr(arr, test_method)(**kwargs)
    if test_method != "to_list":
        result = result.to_list()
    msg = (
        f"dtype - {dtype}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    assert result == expected_value, msg
