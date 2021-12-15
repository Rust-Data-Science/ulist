from typing import List, Union

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
    ],
)
def test_methods(
    test_method: str,
    nums: List[bool],
    expected_value: Union[bool, List[bool]],
):
    dtype = "bool"
    arr = ul.from_iter(nums, dtype=dtype)
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
):
    dtype = "bool"
    arr1 = ul.from_iter(nums, dtype=dtype)
    arr2 = ul.from_iter(other, dtype=dtype)
    result = getattr(arr1, test_method)(arr2)
    check_test_result(dtype, test_method, result, expected_value)
