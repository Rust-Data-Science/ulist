import operator as op
from typing import Callable, List, Union, Optional

import pytest
import ulist as ul
from ulist.utils import check_test_result, expand_dtypes

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[Optional[float]], List[Optional[int]]]


@expand_dtypes
@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value",
    [
        ('argmax', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 4),
        ('argmax', 'float', [5.0, 1.0, 2.0, 3.0, 4.0], 0),
        ('argmax', 'float', [1.0, 2.0, 5.0, 3.0, 4.0], 2),
        ('argmax', 'int', [1, 2, 3, 4, 5], 4),
        ('argmax', 'int', [5, 1, 2, 3, 4], 0),
        ('argmax', 'int', [1, 2, 5, 3, 4], 2),
        ('argmax', 'int', [1, 2, 5, None, 4], 2),
        ('argmax', 'int', [1, 2, None, 3, 4], 4),

        ('argmin', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 0),
        ('argmin', 'float', [2.0, 3.0, 4.0, 5.0, 1.0], 4),
        ('argmin', 'float', [2.0, 5.0, 1.0, 3.0, 4.0], 2),
        ('argmin', 'int', [1, 2, 3, 4, 5], 0),
        ('argmin', 'int', [2, 3, 4, 5, 1], 4),
        ('argmin', 'int', [2, 5, 1, 3, 4], 2),
        ('argmin', 'int', [None, 5, 1, 3, 4], 2),
        ('argmin', 'int', [2, 5, None, 3, 4], 0),

        ('max', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 5.0),
        ('max', 'int', [1, 2, 3, 4, 5], 5),
        ('max', 'int', [1, 2, 3, 4, None], 4),
        ('max', 'int', [1, 2, None, 4, 5], 5),

        ('min', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 1.0),
        ('min', 'int', [1, 2, 3, 4, 5], 1),
        ('min', 'int', [None, 2, 3, 4, 5], 2),
        ('min', 'int', [1, 2, None, 4, 5], 1),
    ],
)
def test_statistics_methods(
    test_method: str,
    dtype: str,
    nums: LIST_TYPE,
    expected_value: NUM_TYPE,
) -> None:
    arr = ul.from_seq(nums, dtype)
    result = getattr(arr, test_method)()
    check_test_result(dtype, test_method, result, expected_value)


@expand_dtypes
@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        (
            'add',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [2.0, 4.0, 6.0, 8.0, 10.0],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'add',
            'int',
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'add',
            'int',
            [1, 2, None, 4, 5],
            [2, 4, None, 8, 10],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'add',
            'int',
            [1, 2, 3, 4, 5],
            [2, 4, None, 8, 10],
            {'other': [1, 2, None, 4, 5]},
        ),
        (
            'add',
            'int',
            [1, 2, None, 4, 5],
            [2, 4, None, 8, 10],
            {'other': [1, 2, None, 4, 5]},
        ),
        (
            'add',
            'int',
            [1, None, 3, 4, 5],
            [2, None, 6, None, 10],
            {'other': [1, 2, 3, None, 5]},
        ),

        (
            'add_scala',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [2.0, 3.0, 4.0, 5.0, 6.0],
            {'elem': 1},
        ),
        (
            'add_scala',
            'int',
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            {'elem': 1},
        ),
        (
            'add_scala',
            'int',
            [1, 2, None, 4, 5],
            [2, 3, None, 5, 6],
            {'elem': 1},
        ),

        (
            'div',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [1.0, 1.0, 1.0, 1.0, 1.0],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'div',
            'int',
            [1, 2, 3, 4, 5],
            [1.0, 1.0, 1.0, 1.0, 1.0],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'div',
            'int',
            [1, 2, None, 4, 5],
            [1.0, 1.0, None, 1.0, 1.0],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'div',
            'int',
            [1, 2, 3, 4, 5],
            [1.0, 1.0, None, 1.0, 1.0],
            {'other': [1, 2, None, 4, 5]},
        ),
        (
            'div',
            'int',
            [1, 2, None, 4, 5],
            [1.0, 1.0, None, 1.0, 1.0],
            {'other': [1, 2, None, 4, 5]},
        ),
        (
            'div',
            'int',
            [1, None, 3, 4, 5],
            [1.0, None, 1.0, None, 1.0],
            {'other': [1, 2, 3, None, 5]},
        ),

        (
            'div_scala',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [0.5, 1.0, 1.5, 2.0, 2.5],
            {'elem': 2}
        ),
        (
            'div_scala',
            'int',
            [1, 2, 3, 4, 5],
            [0.5, 1.0, 1.5, 2.0, 2.5],
            {'elem': 2}
        ),
        (
            'div_scala',
            'int',
            [1, 2, None, 4, 5],
            [0.5, 1.0, None, 2.0, 2.5],
            {'elem': 2}
        ),

        (
            "greater_than_or_equal_scala",
            'float',
            [1.0, 2.0, 3.0],
            [False, True, True],
            {"elem": 2.0}
        ),
        (
            "greater_than_or_equal_scala",
            'int',
            [1, 2, 3],
            [False, True, True],
            {"elem": 2}
        ),
        (
            "greater_than_or_equal_scala",
            'int',
            [1, 2, None],
            [False, True, False],
            {"elem": 2}
        ),

        (
            'greater_than_scala',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [False, False, True, True, True],
            {'elem': 2},
        ),
        (
            'greater_than_scala',
            'int',
            [1, 2, 3, 4, 5],
            [False, False, True, True, True],
            {'elem': 2},
        ),
        (
            'greater_than_scala',
            'int',
            [1, 2, 3, 4, None],
            [False, False, True, True, False],
            {'elem': 2},
        ),

        (
            "less_than_or_equal_scala",
            'float',
            [1.0, 2.0, 3.0],
            [True, True, False],
            {"elem": 2.0},
        ),
        (
            "less_than_or_equal_scala",
            'int',
            [1, 2, 3],
            [True, True, False],
            {"elem": 2},
        ),
        (
            "less_than_or_equal_scala",
            'int',
            [None, 2, 3],
            [False, True, False],
            {"elem": 2},
        ),

        (
            'less_than_scala',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [True, False, False, False, False],
            {'elem': 2},
        ),
        (
            'less_than_scala',
            'int',
            [1, 2, 3, 4, 5],
            [True, False, False, False, False],
            {'elem': 2},
        ),
        (
            'less_than_scala',
            'int',
            [1, 2, None, 4, 5],
            [True, False, False, False, False],
            {'elem': 2},
        ),

        (
            'mul',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [1.0, 4.0, 9.0, 16.0, 25.0],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'mul',
            'int',
            [1, 2, 3, 4, 5],
            [1, 4, 9, 16, 25],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'mul',
            'int',
            [1, 2, None, 4, 5],
            [1, 4, None, 16, 25],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'mul',
            'int',
            [1, 2, 3, 4, 5],
            [1, 4, None, 16, 25],
            {'other': [1, 2, None, 4, 5]},
        ),
        (
            'mul',
            'int',
            [1, 2, None, 4, 5],
            [1, 4, None, 16, 25],
            {'other': [1, 2, None, 4, 5]},
        ),
        (
            'mul',
            'int',
            [1, None, 3, 4, 5],
            [1, None, 9, None, 25],
            {'other': [1, 2, 3, None, 5]},
        ),

        (
            'mul_scala',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [2.0, 4.0, 6.0, 8.0, 10.0],
            {'elem': 2},
        ),
        (
            'mul_scala',
            'int',
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            {'elem': 2},
        ),
        (
            'mul_scala',
            'int',
            [1, 2, None, 4, 5],
            [2, 4, None, 8, 10],
            {'elem': 2},
        ),

        (
            'pow_scala',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [1.0, 4.0, 9.0, 16.0, 25.0],
            {'elem': 2},
        ),
        (
            'pow_scala',
            'int',
            [1, 2, 3, 4, 5],
            [1, 4, 9, 16, 25],
            {'elem': 2},
        ),
        (
            'pow_scala',
            'int',
            [1, 2, None, 4, 5],
            [1, 4, None, 16, 25],
            {'elem': 2},
        ),

        (
            'sub',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [0.0, 0.0, 0.0, 0.0, 0.0],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'sub',
            'int',
            [1, 2, 3, 4, 5],
            [0, 0, 0, 0, 0],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'sub',
            'int',
            [1, 2, None, 4, 5],
            [0, 0, None, 0, 0],
            {'other': [1, 2, 3, 4, 5]},
        ),
        (
            'sub',
            'int',
            [1, 2, 3, 4, 5],
            [0, 0, None, 0, 0],
            {'other': [1, 2, None, 4, 5]},
        ),
        (
            'sub',
            'int',
            [1, 2, None, 4, 5],
            [0, 0, None, 0, 0],
            {'other': [1, 2, None, 4, 5]},
        ),
        (
            'sub',
            'int',
            [1, None, 3, 4, 5],
            [0, None, 0, None, 0],
            {'other': [1, 2, 3, None, 5]},
        ),

        (
            'sub_scala',
            'float',
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [0.0, 1.0, 2.0, 3.0, 4.0],
            {'elem': 1},
        ),
        (
            'sub_scala',
            'int',
            [1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4],
            {'elem': 1},
        ),
        (
            'sub_scala',
            'int',
            [1, 2, None, 4, 5],
            [0, 1, None, 3, 4],
            {'elem': 1},
        ),
    ],
)
def test_arithmetic_methods(
    test_method: str,
    dtype: str,
    nums: LIST_TYPE,
    expected_value: LIST_TYPE,
    kwargs: dict,
) -> None:
    arr = ul.from_seq(nums, dtype)
    if not test_method.endswith("_scala"):
        fn = getattr(arr, test_method)
        if isinstance(kwargs["other"], list):
            result = fn(ul.from_seq(kwargs["other"], dtype))
        else:
            result = fn(kwargs["other"])
    else:
        result = getattr(arr, test_method)(**kwargs)
    check_test_result(dtype, test_method, result, expected_value)


@expand_dtypes
@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        (op.add, 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         2.0, 4.0, 6.0, 8.0, 10.0], {'other': [1, 2, 3, 4, 5]}),
        (op.add, 'float', [1.0, 2.0, 3.0, 4.0, 5.0],
         [2.0, 3.0, 4.0, 5.0, 6.0], {'other': 1}),
        (op.add, 'int', [1, 2, 3, 4, 5], [
         2, 4, 6, 8, 10], {'other': [1, 2, 3, 4, 5]}),
        (op.add, 'int', [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], {'other': 1}),

        (op.ge, 'float', [1.0, 2.0, 3.0], [False, True, True], {"other": 2.0}),
        (op.ge, 'int', [1, 2, 3], [False, True, True], {"other": 2}),

        (op.gt, 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         False, False, True, True, True], {'other': 2}),
        (op.gt, 'int', [1, 2, 3, 4, 5], [
         False, False, True, True, True], {'other': 2}),

        (op.le, 'float', [1.0, 2.0, 3.0], [True, True, False], {"other": 2.0}),
        (op.le, 'int', [1, 2, 3], [True, True, False], {"other": 2}),

        (op.lt, 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         True, False, False, False, False], {'other': 2}),
        (op.lt, 'int', [1, 2, 3, 4, 5], [
         True, False, False, False, False], {'other': 2}),

        (op.mul, 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         1.0, 4.0, 9.0, 16.0, 25.0], {'other': [1, 2, 3, 4, 5]}),
        (op.mul, 'float', [1.0, 2.0, 3.0, 4.0, 5.0],
         [2.0, 4.0, 6.0, 8.0, 10.0], {'other': 2}),
        (op.mul, 'int', [1, 2, 3, 4, 5], [
         1, 4, 9, 16, 25], {'other': [1, 2, 3, 4, 5]}),
        (op.mul, 'int', [1, 2, 3, 4, 5], [2, 4, 6, 8, 10], {'other': 2}),

        (op.pow, 'float', [1.0, 2.0, 3.0], [1.0, 4.0, 9.0], {"other": 2}),
        (op.pow, 'int', [1, 2, 3], [1, 4, 9], {"other": 2}),

        (op.sub, 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         0.0, 0.0, 0.0, 0.0, 0.0], {'other': [1, 2, 3, 4, 5]}),
        (op.sub, 'float', [1.0, 2.0, 3.0, 4.0, 5.0],
         [0.0, 1.0, 2.0, 3.0, 4.0], {'other': 1}),
        (op.sub, 'int', [1, 2, 3, 4, 5], [
         0, 0, 0, 0, 0], {'other': [1, 2, 3, 4, 5]}),
        (op.sub, 'int', [1, 2, 3, 4, 5], [0, 1, 2, 3, 4], {'other': 1}),

        (op.truediv, 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         1.0, 1.0, 1.0, 1.0, 1.0], {'other': [1, 2, 3, 4, 5]}),
        (op.truediv, 'float', [1.0, 2.0, 3.0, 4.0, 5.0],
         [0.5, 1.0, 1.5, 2.0, 2.5], {'other': 2}),
        (op.truediv, 'int', [1, 2, 3, 4, 5], [
         1.0, 1.0, 1.0, 1.0, 1.0], {'other': [1, 2, 3, 4, 5]}),
        (op.truediv, 'int', [1, 2, 3, 4, 5], [
         0.5, 1.0, 1.5, 2.0, 2.5], {'other': 2}),
    ],
)
def test_operators(
    test_method: Callable,
    dtype: str,
    nums: LIST_TYPE,
    expected_value: LIST_TYPE,
    kwargs: dict,
) -> None:
    arr = ul.from_seq(nums, dtype)
    if isinstance(kwargs["other"], list):
        other = ul.from_seq(kwargs["other"], dtype)
    else:
        other = kwargs["other"]
    result = test_method(arr, other)
    check_test_result(dtype, test_method, result, expected_value)
