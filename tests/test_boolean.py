from typing import List, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


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
    ],
)
def test_methods(
    test_method: str,
    nums: List[NUM_TYPE],
    expected_value: LIST_TYPE,
):
    dtype = "bool"
    arr = ul.from_iter(nums, dtype=dtype)
    result = getattr(arr, test_method)()
    check_test_result(dtype, test_method, result, expected_value)
