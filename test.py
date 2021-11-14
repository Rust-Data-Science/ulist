# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-11-14 16:02:00
"""
import pytest
from ulist import FloatList, IntegerList
from typing import Union, List, Optional

LIST_TYPE = Union[FloatList, IntegerList]
NUM_TYPE = Union[float, int]


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
def test(
    test_class: LIST_TYPE,
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
