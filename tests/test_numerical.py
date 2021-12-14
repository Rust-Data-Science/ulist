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
        ('mean', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 3.0),
        ('mean', 'int', [1, 2, 3, 4, 5], 3.0),
        ('min', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 1.0),
        ('min', 'int', [1, 2, 3, 4, 5], 1),
        ('sum', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 15.0),
        ('sum', 'int', [1, 2, 3, 4, 5], 15),
    ],
)
def test_statistics_methods(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: NUM_TYPE,
) -> None:
    arr = ul.from_iter(nums, dtype)
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
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    arr = ul.from_iter(nums, dtype)
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
    nums: List[NUM_TYPE],
    expected_value: LIST_TYPE,
    condition: list,
):
    arr = ul.from_iter(nums, dtype)
    cond = ul.from_iter(condition, dtype="bool")
    result = arr.filter(cond)
    check_test_result(dtype, "filter", result, expected_value)


@ pytest.mark.parametrize(
    "dtype, nums, test_method, expected_value, kwargs",
    [
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "add",
            [2.0, 4.0, 6.0, 8.0, 10.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "sub",
            [0.0, 0.0, 0.0, 0.0, 0.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "mul",
            [1.0, 4.0, 9.0, 16.0, 25.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "div",
            [1.0, 1.0, 1.0, 1.0, 1.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "add_scala",
            [2.0, 3.0, 4.0, 5.0, 6.0],
            {"num": 1},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "sub_scala",
            [0.0, 1.0, 2.0, 3.0, 4.0],
            {"num": 1},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "mul_scala",
            [2.0, 4.0, 6.0, 8.0, 10.0],
            {"num": 2},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "div_scala",
            [0.5, 1.0, 1.5, 2.0, 2.5],
            {"num": 2},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "pow_scala",
            [1.0, 4.0, 9.0, 16.0, 25.0],
            {"num": 2},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "greater_than_scala",
            [False, False, True, True, True],
            {"num": 2},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            "less_than_scala",
            [True, False, False, False, False],
            {"num": 2},
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            "add",
            [2, 4, 6, 8, 10],
            {"other": [1, 2, 3, 4, 5]}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            "sub",
            [0, 0, 0, 0, 0],
            {"other": [1, 2, 3, 4, 5]}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            "mul",
            [1, 4, 9, 16, 25],
            {"other": [1, 2, 3, 4, 5]}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            "div",
            [1.0, 1.0, 1.0, 1.0, 1.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            "add_scala",
            [2, 3, 4, 5, 6],
            {"num": 1}
        ),
        (
            "int", [1, 2, 3, 4, 5],
            "sub_scala",
            [0, 1, 2, 3, 4],
            {"num": 1}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            "mul_scala",
            [2, 4, 6, 8, 10],
            {"num": 2}
        ),
        (
            "int", [1, 2, 3, 4, 5],
            "div_scala",
            [0.5, 1.0, 1.5, 2.0, 2.5],
            {"num": 2}
        ),
        (
            "int", [1, 2, 3, 4, 5],
            "pow_scala",
            [1, 4, 9, 16, 25],
            {"num": 2}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            "greater_than_scala",
            [False, False, True, True, True],
            {"num": 2},
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            "less_than_scala",
            [True, False, False, False, False],
            {"num": 2},
        ),
    ],


)
def test_arithmetic_methods(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    arr = ul.from_iter(nums, dtype)
    if not test_method.endswith("_scala"):
        fn = getattr(arr, test_method)
        if isinstance(kwargs["other"], list):
            result = fn(ul.from_iter(kwargs["other"], dtype))
        else:
            result = fn(kwargs["other"])
    else:
        result = getattr(arr, test_method)(**kwargs)
    check_test_result(dtype, test_method, result, expected_value)


@ pytest.mark.parametrize(
    "dtype, nums, test_method, expected_value, kwargs",
    [
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.add,
            [2.0, 4.0, 6.0, 8.0, 10.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.sub,
            [0.0, 0.0, 0.0, 0.0, 0.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.mul,
            [1.0, 4.0, 9.0, 16.0, 25.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.truediv,
            [1.0, 1.0, 1.0, 1.0, 1.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.add,
            [2.0, 3.0, 4.0, 5.0, 6.0],
            {"other": 1},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.sub,
            [0.0, 1.0, 2.0, 3.0, 4.0],
            {"other": 1},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.mul,
            [2.0, 4.0, 6.0, 8.0, 10.0],
            {"other": 2},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.truediv,
            [0.5, 1.0, 1.5, 2.0, 2.5],
            {"other": 2},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.gt,
            [False, False, True, True, True],
            {"other": 2},
        ),
        (
            "float",
            [1.0, 2.0, 3.0, 4.0, 5.0],
            op.lt,
            [True, False, False, False, False],
            {"other": 2},
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            op.add,
            [2, 4, 6, 8, 10],
            {"other": [1, 2, 3, 4, 5]}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            op.sub,
            [0, 0, 0, 0, 0],
            {"other": [1, 2, 3, 4, 5]}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            op.mul,
            [1, 4, 9, 16, 25],
            {"other": [1, 2, 3, 4, 5]}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            op.truediv,
            [1.0, 1.0, 1.0, 1.0, 1.0],
            {"other": [1, 2, 3, 4, 5]},
        ),
        ("int",
         [1, 2, 3, 4, 5],
         op.add,
         [2, 3, 4, 5, 6],
         {"other": 1}
         ),
        (
            "int",
            [1, 2, 3, 4, 5],
            op.sub,
            [0, 1, 2, 3, 4],
            {"other": 1}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            op.mul,
            [2, 4, 6, 8, 10],
            {"other": 2}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            op.truediv,
            [0.5, 1.0, 1.5, 2.0, 2.5],
            {"other": 2}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            op.gt,
            [False, False, True, True, True],
            {"other": 2}
        ),
        (
            "int",
            [1, 2, 3, 4, 5],
            op.lt,
            [True, False, False, False, False],
            {"other": 2},
        ),
    ],
)
def test_operators(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: Callable,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    arr = ul.from_iter(nums, dtype)
    if isinstance(kwargs["other"], list):
        other = ul.from_iter(kwargs["other"], dtype)
    else:
        other = kwargs["other"]
    result = test_method(arr, other)
    check_test_result(dtype, test_method, result, expected_value)
