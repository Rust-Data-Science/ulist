import operator as op
from typing import Callable, List, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result


@pytest.mark.parametrize(
    "test_method, nums, expected_value, kwargs",
    [
        (
            "equal_scala",
            [1, 2, 3],
            [False, True, False],
            {"num": 2}
        ),
        (
            "not_equal_scala",
            [1, 2, 3],
            [True, False, True],
            {"num": 2}
        ),
        (
            "greater_than_or_equal_scala",
            [1, 2, 3],
            [False, True, True],
            {"num": 2}
        ),
        (
            "less_than_or_equal_scala",
            [1, 2, 3],
            [True, True, False],
            {"num": 2}
        ),
    ],
)
def test_methods(
    test_method: str,
    nums: List[int],
    expected_value: List[bool],
    kwargs: dict,
):
    dtype = "int"
    arr = ul.from_iter(nums, dtype=dtype)
    result = getattr(arr, test_method)(**kwargs).to_list()
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "test_method, nums, expected_value, kwargs",
    [
        (op.eq, [1, 2, 3], [False, True, False], {"other": 2}),
        (op.ne, [1, 2, 3], [True, False, True], {"other": 2}),
        (op.ge, [1, 2, 3], [False, True, True], {"other": 2}),
        (op.le, [1, 2, 3], [True, True, False], {"other": 2}),
    ],
)
def test_operators(
    test_method: Callable,
    nums: List[int],
    expected_value: List[bool],
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
