from typing import List, Union

import pytest
import ulist as ul
import operator as op
from ulist.utils import check_test_result, expand_dtypes

LIST_TYPE = Union[List[float], List[int], List[bool], List[str]]


@expand_dtypes
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
            "float",
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            {
                "conditions": [(op.lt, 2.0), (op.lt, 4.0)],
                "choices": ['foo', 'bar'],
                "default": 'baz',
            },
            ['foo', 'foo', 'bar', 'bar', 'baz', 'baz'],
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
        (
            "int",
            [0, 1, 2, 3, 4, 5],
            {
                "conditions": [(op.lt, 2), (op.lt, 4)],
                "choices": ['foo', 'bar'],
                "default": 'baz',
            },
            ['foo', 'foo', 'bar', 'bar', 'baz', 'baz'],
        ),

        (
            "bool",
            [True, False],
            {
                "conditions": [(op.eq, True)],
                "choices": [False],
                "default": True,
            },
            [False, True],
        ),
        (
            "bool",
            [True, False],
            {
                "conditions": [(op.eq, True)],
                "choices": [0.0],
                "default": 1.0,
            },
            [0.0, 1.0],
        ),
        (
            "bool",
            [True, False],
            {
                "conditions": [(op.eq, True)],
                "choices": [0],
                "default": 1,
            },
            [0, 1],
        ),
        (
            "bool",
            [True, False],
            {
                "conditions": [(op.eq, True)],
                "choices": ['foo'],
                "default": 'bar',
            },
            ['foo', 'bar'],
        ),

        (
            "string",
            ['foo', 'bar'],
            {
                "conditions": [(op.eq, 'foo')],
                "choices": [False],
                "default": True,
            },
            [False, True],
        ),
        (
            "string",
            ['foo', 'bar'],
            {
                "conditions": [(op.eq, 'foo')],
                "choices": [0.0],
                "default": 1.0,
            },
            [0.0, 1.0],
        ),
        (
            "string",
            ['foo', 'bar'],
            {
                "conditions": [(op.eq, 'foo')],
                "choices": [0],
                "default": 1,
            },
            [0, 1],
        ),
        (
            "string",
            ['foo', 'bar'],
            {
                "conditions": [(op.eq, 'foo')],
                "choices": ['foo'],
                "default": 'bar',
            },
            ['foo', 'bar'],
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
        result_dtype = "int"
    elif type(expected_value[0]) == float:
        result_dtype = "float"
    elif type(expected_value[0]) == bool:
        result_dtype = "bool"
    elif type(expected_value[0]) == str:
        result_dtype = "string"
    else:
        raise TypeError(f"Unexpected type {type(expected_value[0])}!")
    check_test_result(result_dtype, "ul.select", result, expected_value)


@expand_dtypes
@pytest.mark.parametrize(
    "dtype, nums, kwargs, expected_value",
    [
        (
            "float",
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            {
                "fn_and_then": [
                    (lambda x: x < 2.0, False),
                    (lambda x: x < 4.0, True),
                ],
                "default": False,
            },
            [False, False, True, True, False, False],
        ),
        (
            "float",
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            {
                "fn_and_then": [
                    (lambda x: x < 2.0, 0.0),
                    (lambda x: x < 4.0, 1.0),
                ],
                "default": 2.0,
            },
            [0.0, 0.0, 1.0, 1.0, 2.0, 2.0],
        ),
        (
            "float",
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            {
                "fn_and_then": [
                    (lambda x: x < 2.0, 0),
                    (lambda x: x < 4.0, 1),
                ],
                "default": 2,
            },
            [0, 0, 1, 1, 2, 2],
        ),
        (
            "float",
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            {
                "fn_and_then": [
                    (lambda x: x < 2.0, 'foo'),
                    (lambda x: x < 4.0, 'bar'),
                ],
                "default": 'baz',
            },
            ['foo', 'foo', 'bar', 'bar', 'baz', 'baz'],
        ),

        (
            "int",
            [0, 1, 2, 3, 4, 5],
            {
                "fn_and_then": [
                    (lambda x: x < 2, False),
                    (lambda x: x < 4, True),
                ],
                "default": False,
            },
            [False, False, True, True, False, False],
        ),
        (
            "int",
            [0, 1, 2, 3, 4, 5],
            {
                "fn_and_then": [
                    (lambda x: x < 2, 0.0),
                    (lambda x: x < 4, 1.0),
                ],
                "default": 2.0,
            },
            [0.0, 0.0, 1.0, 1.0, 2.0, 2.0],
        ),
        (
            "int",
            [0, 1, 2, 3, 4, 5],
            {
                "fn_and_then": [
                    (lambda x: x < 2, 0),
                    (lambda x: x < 4, 1),
                ],
                "default": 2,
            },
            [0, 0, 1, 1, 2, 2],
        ),
        (
            "int",
            [0, 1, 2, 3, 4, 5],
            {
                "fn_and_then": [
                    (lambda x: x < 2, 'foo'),
                    (lambda x: x < 4, 'bar'),
                ],
                "default": 'baz',
            },
            ['foo', 'foo', 'bar', 'bar', 'baz', 'baz'],
        ),

        (
            "bool",
            [True, False],
            {
                "fn_and_then": [
                    (lambda x: x == True, False),  # noqa: E712
                    (lambda x: x == True, False),  # noqa: E712
                ],
                "default": True,
            },
            [False, True],
        ),
        (
            "bool",
            [True, False],
            {
                "fn_and_then": [
                    (lambda x: x == True, 0.0),  # noqa: E712
                    (lambda x: x == True, 0.0),  # noqa: E712
                ],
                "default": 1.0,
            },
            [0.0, 1.0],
        ),
        (
            "bool",
            [True, False],
            {
                "fn_and_then": [
                    (lambda x: x == True, 0),  # noqa: E712
                    (lambda x: x == True, 0),  # noqa: E712
                ],
                "default": 1,
            },
            [0, 1],
        ),
        (
            "bool",
            [True, False],
            {
                "fn_and_then": [
                    (lambda x: x == True, 'foo'),  # noqa: E712
                    (lambda x: x == True, 'foo'),  # noqa: E712
                ],
                "default": 'bar',
            },
            ['foo', 'bar'],
        ),

        (
            "string",
            ['foo', 'bar', 'baz'],
            {
                "fn_and_then": [
                    (lambda x: x == 'foo', True),
                    (lambda x: x == 'bar', False),
                ],
                "default": False,
            },
            [True, False, False],
        ),
        (
            "string",
            ['foo', 'bar', 'baz'],
            {
                "fn_and_then": [
                    (lambda x: x == 'foo', 1.0),
                    (lambda x: x == 'bar', 2.0),
                ],
                "default": 3.0,
            },
            [1.0, 2.0, 3.0],
        ),
        (
            "string",
            ['foo', 'bar', 'baz'],
            {
                "fn_and_then": [
                    (lambda x: x == 'foo', 1),
                    (lambda x: x == 'bar', 2),
                ],
                "default": 3,
            },
            [1, 2, 3],
        ),
        (
            "string",
            ['foo', 'bar', 'baz'],
            {
                "fn_and_then": [
                    (lambda x: x == 'foo', 'abc'),
                    (lambda x: x == 'bar', 'def'),
                ],
                "default": 'ghi',
            },
            ['abc', 'def', 'ghi'],
        ),
    ],
)
def test_case_when(
    dtype: str,
    nums: LIST_TYPE,
    kwargs: dict,
    expected_value: List[bool],
) -> None:
    arr = ul.from_seq(nums, dtype)
    default = kwargs["default"]
    result = arr.case(default)\
        .when(kwargs["fn_and_then"][0][0], then=kwargs["fn_and_then"][0][1])\
        .when(kwargs["fn_and_then"][1][0], then=kwargs["fn_and_then"][1][1])\
        .end()
    if type(expected_value[0]) == int:
        result_dtype = "int"
    elif type(expected_value[0]) == float:
        result_dtype = "float"
    elif type(expected_value[0]) == bool:
        result_dtype = "bool"
    elif type(expected_value[0]) == str:
        result_dtype = "string"
    else:
        raise TypeError(f"Unexpected type {type(expected_value[0])}!")
    check_test_result(result_dtype, "ul.select", result, expected_value)
