import operator as op
from typing import Callable, List, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value",
    [
        ('max', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 5.0),
        ('max', 'int', [1, 2, 3, 4, 5], 5),

        ('min', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 1.0),
        ('min', 'int', [1, 2, 3, 4, 5], 1),
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


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        (
            'sort',
            'float',
            [5.0, 3.0, 2.0, 4.0, 1.0, 3.0],
            [1.0, 2.0, 3.0, 3.0, 4.0, 5.0],
            {'ascending': True}
        ),
        (
            'sort',
            'float',
            [5.0, 3.0, 2.0, 4.0, 1.0, 3.0],
            [5.0, 4.0, 3.0, 3.0, 2.0, 1.0],
            {'ascending': False}
        ),
        (
            'sort',
            'int',
            [5, 3, 2, 4, 1, 3],
            [1, 2, 3, 3, 4, 5],
            {'ascending': True}
        ),
        (
            'sort',
            'int',
            [5, 3, 2, 4, 1, 3],
            [5, 4, 3, 3, 2, 1],
            {'ascending': False}
        ),

        (
            'unique',
            'float',
            [5.0, 3.0, 2.0, 4.0, 1.0, 3.0],
            [1.0, 2.0, 3.0, 4.0, 5.0],
            {}
        ),
        (
            'unique',
            'int',
            [5, 3, 2, 4, 1, 3],
            [1, 2, 3, 4, 5],
            {}
        ),
    ],
)
def test_data_process_methods(
    test_method: str,
    dtype: str,
    nums: LIST_TYPE,
    expected_value: LIST_TYPE,
    kwargs: dict,
) -> None:
    arr = ul.from_seq(nums, dtype)
    result = getattr(arr, test_method)(**kwargs)
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "dtype, nums, expected_value, condition",
    [
        (
            "float",
            [5.0, 3.0, 2.0, 4.0, 1.0, 3.0],
            [5.0, 4.0],
            [True, False, False, True, False, False],
        ),
        (
            "int",
            [5, 3, 2, 4, 1, 3],
            [5, 4],
            [True, False, False, True, False, False],
        ),
    ],
)
def test_filter(
    dtype: str,
    nums: LIST_TYPE,
    expected_value: LIST_TYPE,
    condition: List[bool],
) -> None:
    arr = ul.from_seq(nums, dtype)
    cond = ul.from_seq(condition, dtype="bool")
    result = arr.filter(cond)
    check_test_result(dtype, "filter", result, expected_value)


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        ('add', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         2.0, 4.0, 6.0, 8.0, 10.0], {'other': [1, 2, 3, 4, 5]}),
        ('add', 'int', [1, 2, 3, 4, 5], [
         2, 4, 6, 8, 10], {'other': [1, 2, 3, 4, 5]}),

        ('add_scala', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         2.0, 3.0, 4.0, 5.0, 6.0], {'num': 1}),
        ('add_scala', 'int', [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], {'num': 1}),

        ('div', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         1.0, 1.0, 1.0, 1.0, 1.0], {'other': [1, 2, 3, 4, 5]}),
        ('div', 'int', [1, 2, 3, 4, 5], [
         1.0, 1.0, 1.0, 1.0, 1.0], {'other': [1, 2, 3, 4, 5]}),

        ('div_scala', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         0.5, 1.0, 1.5, 2.0, 2.5], {'num': 2}),
        ('div_scala', 'int', [1, 2, 3, 4, 5], [
         0.5, 1.0, 1.5, 2.0, 2.5], {'num': 2}),

        ("equal_scala", 'float', [1.0, 2.0, 3.0],
         [False, True, False], {"num": 2.0}),
        ("equal_scala", 'int', [1, 2, 3], [False, True, False], {"num": 2}),


        ("greater_than_or_equal_scala", 'float', [
         1.0, 2.0, 3.0], [False, True, True], {"num": 2.0}),
        ("greater_than_or_equal_scala", 'int', [
         1, 2, 3], [False, True, True], {"num": 2}),

        ('greater_than_scala', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         False, False, True, True, True], {'num': 2}),
        ('greater_than_scala', 'int', [1, 2, 3, 4, 5], [
         False, False, True, True, True], {'num': 2}),

        ("less_than_or_equal_scala", 'float', [
         1.0, 2.0, 3.0], [True, True, False], {"num": 2.0}),
        ("less_than_or_equal_scala", 'int', [
         1, 2, 3], [True, True, False], {"num": 2}),

        ('less_than_scala', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         True, False, False, False, False], {'num': 2}),
        ('less_than_scala', 'int', [1, 2, 3, 4, 5], [
         True, False, False, False, False], {'num': 2}),

        ('mul', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         1.0, 4.0, 9.0, 16.0, 25.0], {'other': [1, 2, 3, 4, 5]}),
        ('mul', 'int', [1, 2, 3, 4, 5], [
         1, 4, 9, 16, 25], {'other': [1, 2, 3, 4, 5]}),

        ('mul_scala', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         2.0, 4.0, 6.0, 8.0, 10.0], {'num': 2}),
        ('mul_scala', 'int', [1, 2, 3, 4, 5], [2, 4, 6, 8, 10], {'num': 2}),

        ("not_equal_scala", 'float', [1.0, 2.0, 3.0], [
         True, False, True], {"num": 2.0}),
        ("not_equal_scala", 'int', [1, 2, 3], [True, False, True], {"num": 2}),

        ('pow_scala', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         1.0, 4.0, 9.0, 16.0, 25.0], {'num': 2}),
        ('pow_scala', 'int', [1, 2, 3, 4, 5], [1, 4, 9, 16, 25], {'num': 2}),

        ('sub', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         0.0, 0.0, 0.0, 0.0, 0.0], {'other': [1, 2, 3, 4, 5]}),
        ('sub', 'int', [1, 2, 3, 4, 5], [
         0, 0, 0, 0, 0], {'other': [1, 2, 3, 4, 5]}),

        ('sub_scala', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         0.0, 1.0, 2.0, 3.0, 4.0], {'num': 1}),
        ('sub_scala', 'int', [1, 2, 3, 4, 5], [0, 1, 2, 3, 4], {'num': 1}),
    ],


)
def test_arithmetic_methods(
    test_method: str,
    dtype: str,
    nums: List[NUM_TYPE],
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


@ pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        (op.add, 'float', [1.0, 2.0, 3.0, 4.0, 5.0], [
         2.0, 4.0, 6.0, 8.0, 10.0], {'other': [1, 2, 3, 4, 5]}),
        (op.add, 'float', [1.0, 2.0, 3.0, 4.0, 5.0],
         [2.0, 3.0, 4.0, 5.0, 6.0], {'other': 1}),
        (op.add, 'int', [1, 2, 3, 4, 5], [
         2, 4, 6, 8, 10], {'other': [1, 2, 3, 4, 5]}),
        (op.add, 'int', [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], {'other': 1}),

        (op.eq, 'float', [1.0, 2.0, 3.0], [
         False, True, False], {"other": 2.0}),
        (op.eq, 'int', [1, 2, 3], [False, True, False], {"other": 2}),

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

        (op.ne, 'float', [1.0, 2.0, 3.0], [True, False, True], {"other": 2.0}),
        (op.ne, 'int', [1, 2, 3], [True, False, True], {"other": 2}),

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
    nums: List[NUM_TYPE],
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
