from typing import List, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result

NUM_TYPE = Union[float, int, bool]
LIST_TYPE = Union[List[float], List[int], List[bool]]
NUM_OR_LIST_TYPE = Union[NUM_TYPE, LIST_TYPE]


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value",
    [
        (
            "__repr__",
            "bool",
            [True, False] * 50,
            "UltraFastList([True, False, True, ..., False, True, False])",
        ),
        ('__repr__', 'bool', [True, False], 'UltraFastList([True, False])'),
        ('__repr__', 'float', [1.0, 2.0], 'UltraFastList([1.0, 2.0])'),
        ('__repr__', 'float', range(0, 100),
         'UltraFastList([0.0, 1.0, 2.0, ..., 97.0, 98.0, 99.0])'),
        ('__repr__', 'int', [1, 2], 'UltraFastList([1, 2])'),
        ('__repr__', 'int', range(0, 100),
         'UltraFastList([0, 1, 2, ..., 97, 98, 99])'),

        (
            "__str__",
            "bool",
            [True, False] * 50,
            "[True, False, True, ..., False, True, False]",
        ),
        ('__str__', 'bool', [True, False], '[True, False]'),
        ('__str__', 'float', [1.0, 2.0], '[1.0, 2.0]'),
        ('__str__', 'float', range(0, 100),
         '[0.0, 1.0, 2.0, ..., 97.0, 98.0, 99.0]'),
        ('__str__', 'int', [1, 2], '[1, 2]'),
        ('__str__', 'int', range(0, 100), '[0, 1, 2, ..., 97, 98, 99]'),

        ('copy', 'bool', [True, False], [True, False]),
        ('copy', 'float', [1.0, 2.0], [1.0, 2.0]),
        ('copy', 'int', [1, 2], [1, 2]),

        ('mean', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 3.0),
        ('mean', 'int', [1, 2, 3, 4, 5], 3.0),
        ('mean', 'bool', [True, False, True, False], 0.5),

        ('size', 'bool', [True, False], 2),
        ('size', 'float', [1.0, 2.0], 2),
        ('size', 'int', [1, 2], 2),

        ('sum', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 15.0),
        ('sum', 'int', [1, 2, 3, 4, 5], 15),
        ('sum', 'bool', [True, False, True], 2,),

        ('to_list', 'bool', [True, False], [True, False]),
        ('to_list', 'bool', [True, False], [True, False]),
        ('to_list', 'float', [1.0, 2.0], [1.0, 2.0]),
        ('to_list', 'int', [1, 2], [1, 2]),
    ],
)
def test_methods_no_arg(
    test_method: str,
    dtype: str,
    nums: LIST_TYPE,
    expected_value: NUM_OR_LIST_TYPE,
) -> None:
    arr = ul.from_seq(nums, dtype)
    result = getattr(arr, test_method)()
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        ('__getitem__', 'bool', [True, False, True], True, {'index': 2}),
        ('__getitem__', 'float', [1.0, 2.0, 3.0], 2.0, {'index': 1}),
        ('__getitem__', 'int', [1, 2, 3], 1, {'index': 0}),

        ('astype', 'bool', [True, False], [1, 0], {'dtype': 'int'}),
        ('astype', 'bool', [True, False], [1.0, 0.0], {'dtype': 'float'}),
        ('astype', 'bool', [True, False], [True, False], {'dtype': 'bool'}),

        ('astype', 'float', [1.0, 2.0, 3.0], [1, 2, 3], {'dtype': 'int'}),
        ('astype', 'float', [1.0, 2.0, 3.0], [
         1.0, 2.0, 3.0], {'dtype': 'float'}),
        ('astype', 'float', [-2.0, -1.0, 0.0, 1.0, 2.0],
         [True, True, False, True, True], {'dtype': 'bool'}),

        ('astype', 'int', [1, 2, 3], [1, 2, 3], {'dtype': 'int'}),
        ('astype', 'int', [1, 2, 3], [1.0, 2.0, 3.0], {'dtype': 'float'}),
        ('astype', 'int', [-2, -1, 0, 1, 2],
         [True, True, False, True, True], {'dtype': 'bool'}),

        ('get', 'bool', [True, False, True], True, {'index': 2}),
        ('get', 'float', [1.0, 2.0, 3.0], 2.0, {'index': 1}),
        ('get', 'int', [1, 2, 3], 1, {'index': 0}),

        ('replace', 'bool', [True, False, True], [
         False, False, False], {'old': True, 'new': False}),
        ('replace', 'float', [1.0, 0.0, 1.0], [
         0.0, 0.0, 0.0], {'old': 1.0, 'new': 0.0}),
        ('replace', 'int', [1, 0, 1], [0, 0, 0], {'old': 1, 'new': 0}),
    ],
)
def test_methods_with_args(
    test_method: str,
    dtype: str,
    nums: LIST_TYPE,
    expected_value: NUM_OR_LIST_TYPE,
    kwargs: dict,
) -> None:
    arr = ul.from_seq(nums, dtype)
    result = getattr(arr, test_method)(**kwargs)
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        ('__setitem__', 'bool', [True, False], [
            True, True], {'index': 1, 'num': True}),
        ('__setitem__', 'float', [1.0, 2.0], [
         1.0, 3.0], {'index': 1, 'num': 3.0}),
        ('__setitem__', 'int', [1, 2], [1, 3], {'index': 1, 'num': 3}),

        ('append', 'bool', [True], [True, False], {'num': False}),
        ('append', 'float', [1.0], [1.0, 2.0], {'num': 2.0}),
        ('append', 'int', [1], [1, 2], {'num': 2}),

        ('pop', 'bool', [True, False], [True], {}),
        ('pop', 'float', [1.0, 2.0], [1.0], {}),
        ('pop', 'int', [1, 2], [1], {}),

        ('set', 'bool', [True, False], [
         True, True], {'index': 1, 'num': True}),
        ('set', 'float', [1.0, 2.0], [1.0, 3.0], {'index': 1, 'num': 3.0}),
        ('set', 'int', [1, 2], [1, 3], {'index': 1, 'num': 3}),
    ],
)
def test_multable_methods(
    test_method: str,
    dtype: str,
    nums: LIST_TYPE,
    expected_value: LIST_TYPE,
    kwargs: dict,
) -> None:
    arr = ul.from_seq(nums, dtype)
    getattr(arr, test_method)(**kwargs)
    check_test_result(dtype, test_method, arr, expected_value)


@pytest.mark.parametrize(
    "dtype, nums, expected_value, kwargs",
    [
        ('bool', [True, False], [True, True], {'index': 1, 'num': True}),
        ('float', [1.0, 2.0], [1.0, 3.0], {'index': 1, 'num': 3.0}),
        ('int', [1, 2], [1, 3], {'index': 1, 'num': 3}),
    ],
)
def test_indexing_operations(
    dtype: str,
    nums: LIST_TYPE,
    expected_value: LIST_TYPE,
    kwargs: dict,
) -> None:
    index = kwargs["index"]
    num = kwargs["num"]
    # Set
    test_method = "set-item"
    arr = ul.from_seq(nums, dtype)
    arr[index] = num
    check_test_result(dtype, test_method, arr, expected_value)

    # Get
    test_method = "get-item"
    expected_value = kwargs["num"]
    result = arr[index]
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "dtype, nums, expected_dtype",
    [
        ('bool', [True, False], 'int'),
        ('bool', [True, False], 'float'),
        ('bool', [True, False], 'bool'),

        ('float', [1.0, 2.0], 'int'),
        ('float', [1.0, 2.0], 'float'),
        ('float', [1.0, 2.0], 'bool'),

        ('int', [1, 2], 'int'),
        ('int', [1, 2], 'float'),
        ('int', [1, 2], 'bool'),
    ],
)
def test_astype(
    dtype: str,
    nums: LIST_TYPE,
    expected_dtype: str,
) -> None:
    """
    The output of `astype` is already tested in `test_methods_with_args`.
    We run additional tests here:
        1. The astype method should return a new ulist object;
        2. The returned object should has correct dtype;
    """
    arr = ul.from_seq(nums, dtype=dtype)
    result = arr.astype(expected_dtype)
    assert result.dtype == expected_dtype
    assert id(result) != id(arr)
