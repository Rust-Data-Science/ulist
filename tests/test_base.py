from typing import List, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value",
    [
        (
            "__str__",
            "bool",
            [True, False] * 50,
            "UltraFastList([True, False, True, ..., False, True, False])",
        ),
        ('__str__', 'bool', [True, False], 'UltraFastList([True, False])'),
        ('__str__', 'float', [1.0, 2.0], 'UltraFastList([1.0, 2.0])'),
        ('__str__', 'float', range(0, 100),
         'UltraFastList([0.0, 1.0, 2.0, ..., 97.0, 98.0, 99.0])'),
        ('__str__', 'int', [1, 2], 'UltraFastList([1, 2])'),
        ('__str__', 'int', range(0, 100),
         'UltraFastList([0, 1, 2, ..., 97, 98, 99])'),
        ('copy', 'bool', [True, False], [True, False]),
        ('copy', 'float', [1.0, 2.0], [1.0, 2.0]),
        ('copy', 'int', [1, 2], [1, 2]),
        ('size', 'bool', [True, False], 2),
        ('size', 'float', [1.0, 2.0], 2),
        ('size', 'int', [1, 2], 2),
        ('to_list', 'bool', [True, False], [True, False]),
        ('to_list', 'bool', [True, False], [True, False]),
        ('to_list', 'float', [1.0, 2.0], [1.0, 2.0]),
        ('to_list', 'int', [1, 2], [1, 2]),
    ],
)
def test_methods_no_arg(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
):
    arr = ul.from_iter(nums, dtype)
    result = getattr(arr, test_method)()
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        ('__getitem__', 'bool', [True, False, True], True, {'index': 2}),
        ('__getitem__', 'float', [1.0, 2.0, 3.0], 2.0, {'index': 1}),
        ('__getitem__', 'int', [1, 2, 3], 1, {'index': 0}),
        ('get', 'bool', [True, False, True], True, {'index': 2}),
        ('get', 'float', [1.0, 2.0, 3.0], 2.0, {'index': 1}),
        ('get', 'int', [1, 2, 3], 1, {'index': 0}),
    ],
)
def test_methods_with_args(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
    kwargs: dict,
):
    arr = ul.from_iter(nums, dtype)
    result = getattr(arr, test_method)(**kwargs)
    check_test_result(dtype, test_method, result, expected_value)
