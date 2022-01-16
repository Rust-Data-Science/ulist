from typing import List, Union

import pytest
import ulist as ul
import operator as op
from ulist.utils import check_test_result

LIST_TYPE = Union[List[float], List[int], List[bool]]


@pytest.mark.parametrize(
    "dtype, nums, kwargs, expected_value",
    [
        (
            "float",
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            {
                "conditions": [(op.lt, 2.0), (op.lt, 4.0)],
                "choices": [False, True],
                "default": False,
            },
            [False, False, True, True, False, False],
        ),
        (
            "float",
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            {
                "conditions": [(op.lt, 2.0), (op.lt, 4.0)],
                "choices": [0.0, 1.0],
                "default": 2.0,
            },
            [0.0, 0.0, 1.0, 1.0, 2.0, 2.0],
        ),
        (
            "float",
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            {
                "conditions": [(op.lt, 2.0), (op.lt, 4.0)],
                "choices": [0, 1],
                "default": 2,
            },
            [0, 0, 1, 1, 2, 2],
        ),

        (
            "int",
            [0, 1, 2, 3, 4, 5],
            {
                "conditions": [(op.lt, 2), (op.lt, 4)],
                "choices": [False, True],
                "default": False,
            },
            [False, False, True, True, False, False],
        ),
        (
            "int",
            [0, 1, 2, 3, 4, 5],
            {
                "conditions": [(op.lt, 2), (op.lt, 4)],
                "choices": [0.0, 1.0],
                "default": 2.0,
            },
            [0.0, 0.0, 1.0, 1.0, 2.0, 2.0],
        ),
        (
            "int",
            [0, 1, 2, 3, 4, 5],
            {
                "conditions": [(op.lt, 2), (op.lt, 4)],
                "choices": [0, 1],
                "default": 2,
            },
            [0, 0, 1, 1, 2, 2],
        ),
    ],
)
def test_select(
    dtype: str,
    nums: LIST_TYPE,
    kwargs: dict,
    expected_value: List[bool],
) -> None:
    arr = ul.from_seq(nums, dtype)
    choices = kwargs["choices"]
    default = kwargs["default"]
    conditions = [f(arr, v) for f, v in kwargs["conditions"]]
    result = ul.select(conditions, choices=choices, default=default)
    if type(expected_value[0]) == int:
        dtype = "int"
    elif type(expected_value[0]) == float:
        dtype = "float"
    elif type(expected_value[0]) == bool:
        dtype = "bool"
    else:
        raise TypeError(f"Unexpected type {type(expected_value[0])}!")
    check_test_result(dtype, "ul.select", result, expected_value)
