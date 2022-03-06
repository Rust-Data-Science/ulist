import operator as op
from typing import Callable, List, Optional, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result


@pytest.mark.parametrize(
    "test_method, nums, expected_value",
    [
        (
            "all",
            [False, False, False],
            False,
        ),
        (
            "all",
            [True, False, True],
            False,
        ),
        (
            "all",
            [True, True, True],
            True,
        ),

        (
            "any",
            [False, False, False],
            False,
        ),
        (
            "any",
            [True, False, True],
            True,
        ),
        (
            "any",
            [True, True, True],
            True,
        ),

        (
            "not_",
            [True, False],
            [False, True],
        ),
        (
            "to_index",
            [True, False, True],
            [0, 2],
        )

    ],
)
def test_methods(
    test_method: str,
    nums: List[bool],
    expected_value: Union[bool, List[bool]],
) -> None:
    dtype = "bool"
    arr = ul.from_seq(nums, dtype=dtype)
    result = getattr(arr, test_method)()
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "test_method, nums, other, expected_value",
    [
        (
            "and_",
            [False, False, True, True],
            [False, True, False, True],
            [False, False, False, True],
        ),
        (
            "or_",
            [False, False, True, True],
            [False, True, False, True],
            [False, True, True, True],
        ),
    ],
)
def test_methods_with_args(
    test_method: str,
    nums: List[bool],
    other: List[bool],
    expected_value: List[bool],
) -> None:
    dtype = "bool"
    arr1 = ul.from_seq(nums, dtype=dtype)
    arr2 = ul.from_seq(other, dtype=dtype)
    result = getattr(arr1, test_method)(arr2)
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "test_method, nums, other, expected_value",
    [
        (
            op.and_,
            [True, True, False, False],
            [True, False, True, False],
            [True, False, False, False],
        ),
        (
            op.invert,
            [True, False],
            None,
            [False, True],
        ),
        (
            op.or_,
            [True, True, False, False],
            [True, False, True, False],
            [True, True, True, False],
        ),
    ],
)
def test_operators(
    test_method: Callable,
    nums: List[bool],
    other: Optional[List[bool]],
    expected_value: List[bool],
) -> None:
    dtype = "bool"
    arr1 = ul.from_seq(nums, dtype)
    if other is not None:
        arr2 = ul.from_seq(other, dtype)
        result = test_method(arr1, arr2)
    else:
        result = test_method(arr1)
    check_test_result(dtype, test_method, result, expected_value)
