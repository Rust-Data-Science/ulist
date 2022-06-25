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
            [True, True, True],
            True,
        ),
        (
            'all',
            [True, True, False],
            False,
        ),
        (
            'all',
            [True, True, None],
            None,
        ),
        (
            'all',
            [True, False, True],
            False,
        ),
        (
            'all',
            [True, False, False],
            False,
        ),
        (
            'all',
            [True, False, None],
            False,
        ),
        (
            'all',
            [True, None, True],
            None,
        ),
        (
            'all',
            [True, None, False],
            False,
        ),
        (
            'all',
            [True, None, None],
            None,
        ),
        (
            'all',
            [False, True, True],
            False,
        ),
        (
            'all',
            [False, True, False],
            False,
        ),
        (
            'all',
            [False, True, None],
            False,
        ),
        (
            'all',
            [False, False, True],
            False,
        ),
        (
            'all',
            [False, False, False],
            False,
        ),
        (
            'all',
            [False, False, None],
            False,
        ),
        (
            'all',
            [False, None, True],
            False,
        ),
        (
            'all',
            [False, None, False],
            False,
        ),
        (
            'all',
            [False, None, None],
            False,
        ),
        (
            'all',
            [None, True, True],
            None,
        ),
        (
            'all',
            [None, True, False],
            False,
        ),
        (
            'all',
            [None, True, None],
            None,
        ),
        (
            'all',
            [None, False, True],
            False,
        ),
        (
            'all',
            [None, False, False],
            False,
        ),
        (
            'all',
            [None, False, None],
            False,
        ),
        (
            'all',
            [None, None, True],
            None,
        ),
        (
            'all',
            [None, None, False],
            False,
        ),
        (
            'all',
            [None, None, None],
            None,
        ),

        (
            'any',
            [True, True, True],
            True,
        ),
        (
            'any',
            [True, True, False],
            True,
        ),
        (
            'any',
            [True, True, None],
            True,
        ),
        (
            'any',
            [True, False, True],
            True,
        ),
        (
            'any',
            [True, False, False],
            True,
        ),
        (
            'any',
            [True, False, None],
            True,
        ),
        (
            'any',
            [True, None, True],
            True,
        ),
        (
            'any',
            [True, None, False],
            True,
        ),
        (
            'any',
            [True, None, None],
            True,
        ),
        (
            'any',
            [False, True, True],
            True,
        ),
        (
            'any',
            [False, True, False],
            True,
        ),
        (
            'any',
            [False, True, None],
            True,
        ),
        (
            'any',
            [False, False, True],
            True,
        ),
        (
            'any',
            [False, False, False],
            False,
        ),
        (
            'any',
            [False, False, None],
            None,
        ),
        (
            'any',
            [False, None, True],
            True,
        ),
        (
            'any',
            [False, None, False],
            None,
        ),
        (
            'any',
            [False, None, None],
            None,
        ),
        (
            'any',
            [None, True, True],
            True,
        ),
        (
            'any',
            [None, True, False],
            True,
        ),
        (
            'any',
            [None, True, None],
            True,
        ),
        (
            'any',
            [None, False, True],
            True,
        ),
        (
            'any',
            [None, False, False],
            None,
        ),
        (
            'any',
            [None, False, None],
            None,
        ),
        (
            'any',
            [None, None, True],
            True,
        ),
        (
            'any',
            [None, None, False],
            None,
        ),
        (
            'any',
            [None, None, None],
            None,
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
            [True, True, True, False, False, False, None, None, None],
            [True, False, None, True, False, None, True, False, None],
            [True, True, True, True, False, None, True, None, None],
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


@pytest.mark.parametrize(
    "test_method, nums, other, expected_value",
    [
        (
            op.and_,
            [False, False, True, True],
            [False, True, False, True],
            [False, False, False, True],
        ),
        (
            op.and_,
            [True, True, True, False, False, False, None, None, None],
            [True, False, None, True, False, None, True, False, None],
            [True, False, None, False, False, False, None, False, None],
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
            [False, False, True, True],
            [False, True, False, True],
            [False, True, True, True],
        ),
        (
            op.or_,
            [True, True, True, False, False, False, None, None, None],
            [True, False, None, True, False, None, True, False, None],
            [True, True, True, True, False, None, True, None, None],
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
