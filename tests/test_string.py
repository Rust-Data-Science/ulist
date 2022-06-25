from typing import List, Union, Optional

import pytest
import ulist as ul
from ulist.utils import check_test_result

LIST_TYPE = Union[List[float], List[int], List[bool], List[str]]


@pytest.mark.parametrize(
    "test_method, nums, expected_value, kwargs",
    [
        (
            "contains",
            ["num1", "num2", "element1", "element2"],
            [True, True, False, False],
            {"elem": "num"},
        ),
        (
            "contains",
            ["num1", "num2", "element1", None],
            [True, True, False, None],
            {"elem": "num"},
        ),

        (
            "starts_with",
            ["num", "1num2", "3num", "num1"],
            [True, False, False, True],
            {"elem": "num"},
        ),
        (
            "starts_with",
            ["num", "1num2", "3num", "num1", None],
            [True, False, False, True, None],
            {"elem": "num"},
        ),

        (
            "ends_with",
            ["num", "1num2", "3num", "num1"],
            [True, False, True, False],
            {"elem": "num"},
        ),
        (
            "ends_with",
            ["num", "1num2", "3num", "num1", None],
            [True, False, True, False, None],
            {"elem": "num"},
        ),

        (
            "str_len",
            ["num", "1num", "", "*", " ", "sp ace", "ta	b"],
            [3, 4, 0, 1, 1, 6, 4],
            {}
        ),
        (
            "str_len",
            ["num", "1num", "", "*", " ", "sp ace", "ta	b", None],
            [3, 4, 0, 1, 1, 6, 4, None],
            {}
        ),
    ],
)
def test_methods_with_args(
    test_method: str,
    nums: List[str],
    expected_value: List[Optional[str]],
    kwargs: dict,
) -> None:
    dtype = "string"
    arr = ul.from_seq(nums, dtype=dtype)
    result = getattr(arr, test_method)(**kwargs)
    check_test_result(dtype, test_method, result, expected_value)
