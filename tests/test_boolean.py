import operator as op
from typing import Callable, List, Optional, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result


@pytest.mark.parametrize(
    "test_method, nums, expected_value",
    [
        (
            'all',
            [False, False, False],
            False,
        ),
        # TODO: Add tests cases for 'all'

        (
            'any',
            [False, False, False],
            False,
        ),
        (
            'any',
            [True, False, True],
            True,
        ),
        (
            'any',
            [True, True, True],
            True,
        ),
        (
            'any',
            [True, True, None],
            True,
        ),
        (
            'any',
            [True, False, None],
            True,
        ),
        (
            'any',
            [False, False, None],
            False,
        ),

        (
            'not_',
            [True, False],
            [False, True],
        ),
        (
            'not_',
            [True, False, None],
            [False, True, None],
        ),

        (
            'to_index',
            [True, False, True],
            [0, 2],
        ),
        (
            'to_index',
            [True, False, True, None],
            [0, 2],
        ),
    ],
)
def test_methods(
    test_method: str,
    nums: List[bool],
    expected_value: Union[Optional[bool], List[Optional[bool]]],
) -> None:
    dtype = "bool"
    arr = ul.from_seq(nums, dtype=dtype)
    result = getattr(arr, test_method)()
    check_test_result(dtype, test_method, result, expected_value)


@ pytest.mark.parametrize(
    "test_method, nums, other, expected_value",
    [
        (
            'and_',
            [False, False, True, True],
            [False, True, False, True],
            [False, False, False, True],
        ),
        (
            'and_',
            [True, True, True, False, False, False, None, None, None],
            [True, False, None, True, False, None, True, False, None],
            [True, False, None, False, False, False, None, False, None],
        ),

        (
            'or_',
            [False, False, True, True],
            [False, True, False, True],
            [False, True, True, True],
        ),
        (
            'or_',
            [False, False, True, True, None, None],
            [False, True, False, True, True, False],
            [False, True, True, True, True, False],
        ),
    ],
)
def test_methods_with_args(
    test_method: str,
    nums: List[bool],
    other: List[bool],
    expected_value: List[Optional[bool]],
) -> None:
    dtype = "bool"
    arr1 = ul.from_seq(nums, dtype=dtype)
    arr2 = ul.from_seq(other, dtype=dtype)
    result = getattr(arr1, test_method)(arr2)
    check_test_result(dtype, test_method, result, expected_value)


@ pytest.mark.parametrize(
    "test_method, nums, other, expected_value",
    [
        (
            op.and_,
            [True, True, False, False],
            [True, False, True, False],
            [True, False, False, False],
        ),
        (
            op.and_,
            [False, False, True, True, None, None],
            [False, True, False, True, True, False],
            [False, False, False, True, False, False],
        ),

        (
            op.invert,
            [True, False],
            None,
            [False, True],
        ),
        (
            op.invert,
            [True, False, None],
            None,
            [False, True, None],
        ),

        (
            op.or_,
            [True, True, False, False],
            [True, False, True, False],
            [True, True, True, False],
        ),
        (
            op.or_,
            [False, False, True, True, None, None],
            [False, True, False, True, True, False],
            [False, True, True, True, True, False],
        ),
    ],
)
def test_operators(
    test_method: Callable,
    nums: List[bool],
    other: Optional[List[bool]],
    expected_value: List[Optional[bool]],
) -> None:
    dtype = "bool"
    arr1 = ul.from_seq(nums, dtype)
    if other is not None:
        arr2 = ul.from_seq(other, dtype)
        result = test_method(arr1, arr2)
    else:
        result = test_method(arr1)
    check_test_result(dtype, test_method, result, expected_value)
