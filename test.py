# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-11-14 16:02:00
"""
import pytest
from ulist import FloatList, IntegerList, BooleanList
from typing import Union, List, Optional

ULIST_TYPE = Union[FloatList, IntegerList]
NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


@pytest.mark.parametrize(
    "test_class, nums",
    [(FloatList, [1.0, 2.0, 3.0, 4.0, 5.0]), (IntegerList, [1, 2, 3, 4, 5])],
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
    test_class: ULIST_TYPE,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: NUM_TYPE,
    expected_type: Optional[NUM_TYPE],
) -> None:
    arr = test_class(nums)
    result = getattr(arr, test_method)()
    msg = (
        f"test_class - {test_class}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    assert result == expected_value, msg

    if expected_type is None:
        if test_class is FloatList:
            expected_type = float
        elif test_class is IntegerList:
            expected_type = int
    assert type(result) == expected_type, msg

    assert len(arr) == arr.size()


@pytest.mark.parametrize(
    "test_class, nums",
    [(FloatList, [5.0, 3.0, 2.0, 4.0, 1.0, 3.0]), (IntegerList, [5, 3, 2, 4, 1, 3])],
)
@pytest.mark.parametrize(
    "test_method, expected_value, kwargs",
    [
        ("copy", [5, 3, 2, 4, 1, 3], {}),
        (
            "filter",
            [5, 4],
            {"condition": BooleanList([True, False, False, True, False, False])},
        ),
        ("sort", [1, 2, 3, 3, 4, 5], {"ascending": True}),
        ("sort", [5, 4, 3, 3, 2, 1], {"ascending": False}),
        ("to_list", [5, 3, 2, 4, 1, 3], {}),
        ("unique", [1, 2, 3, 4, 5], {}),
    ],
)
def test_data_process_methods(
    test_class: ULIST_TYPE,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    arr = test_class(nums)
    result = getattr(arr, test_method)(**kwargs)
    if test_method != "to_list":
        result = result.to_list()
    msg = (
        f"test_class - {test_class}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    assert result == expected_value, msg


@pytest.mark.parametrize(
    "test_class, nums",
    [(FloatList, [1.0, 2.0, 3.0, 4.0, 5.0]), (IntegerList, [1, 2, 3, 4, 5])],
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
    ],
)
def test_arithmetic_methods(
    test_class: ULIST_TYPE,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    arr = test_class(nums)
    if test_method in ("add", "sub", "mul", "div"):
        result = getattr(arr, test_method)(test_class(kwargs["other"]))
    else:
        result = getattr(arr, test_method)(**kwargs)
    if test_method != "to_list":
        result = result.to_list()
    msg = (
        f"test_class - {test_class}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    assert result == expected_value, msg
