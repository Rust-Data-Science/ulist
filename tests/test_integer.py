import operator as op
from typing import Callable, List, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


@pytest.mark.parametrize(
    "nums, test_method, expected_value, kwargs",
    [
        (
            [1, 2, 3],
            "equal_scala",
            [False, True, False],
            {"num": 2}
        ),
        (
            [1, 2, 3],
            "not_equal_scala",
            [True, False, True],
            {"num": 2}
        ),
        (
            [1, 2, 3],
            "greater_than_or_equal_scala",
            [False, True, True],
            {"num": 2}
        ),
        (
            [1, 2, 3],
            "less_than_or_equal_scala",
            [True, True, False],
            {"num": 2}
        ),
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
    result = getattr(arr, test_method)(**kwargs).to_list()
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "nums, test_method, expected_value, kwargs",
    [
        ([1, 2, 3], op.eq, [False, True, False], {"other": 2}),
        ([1, 2, 3], op.ne, [True, False, True], {"other": 2}),
        ([1, 2, 3], op.ge, [False, True, True], {"other": 2}),
        ([1, 2, 3], op.le, [True, True, False], {"other": 2}),
    ],
)
def test_operators(
    nums: List[NUM_TYPE],
    test_method: Callable,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    dtype = "int"
    arr = ul.from_iter(nums, dtype)
    if isinstance(kwargs["other"], list):
        other = ul.from_iter(kwargs["other"], dtype)
    else:
        other = kwargs["other"]
    result = test_method(arr, other)
    check_test_result(dtype, test_method, result, expected_value)
