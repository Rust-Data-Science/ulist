from typing import Dict, List, Union

import pytest
import ulist as ul
from ulist.utils import check_test_result

ELEM_TYPE = Union[float, int, bool, str]
LIST_TYPE = Union[List[float], List[int], List[bool], List[str]]
COUNTER = Union[Dict[int, int], Dict[bool, int]]
RESULT = Union[ELEM_TYPE, LIST_TYPE, COUNTER]


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value",
    [
        ('__len__', 'float', [1.0, 2.0, 3.0], 3),
        ('__len__', 'int', [1, 2, 3], 3),
        ('__len__', 'bool', [True, False, True], 3),
        ('__len__', 'str', ['foo', 'bar', 'baz'], 3),

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
            "__repr__",
            "str",
            ['foo', 'bar'] * 50,
            "UltraFastList(['foo', 'bar', 'foo', ..., 'bar', 'foo', 'bar'])",
        ),
        ('__repr__', 'str', ['foo', 'bar'], "UltraFastList(['foo', 'bar'])"),

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
        (
            "__str__",
            "str",
            ['foo', 'bar'] * 50,
            "['foo', 'bar', 'foo', ..., 'bar', 'foo', 'bar']",
        ),
        ('__str__', 'str', ['foo', 'bar'], "['foo', 'bar']"),

        ('copy', 'bool', [True, False], [True, False]),
        ('copy', 'float', [1.0, 2.0], [1.0, 2.0]),
        ('copy', 'int', [1, 2], [1, 2]),
        ('copy', 'str', ['foo', 'bar'], ['foo', 'bar']),

        ('counter', 'bool', [True, False, True], {True: 2, False: 1}),
        ('counter', 'int', [1, 0, 1], {1: 2, 0: 1}),
        ('counter', 'str', ['foo', 'bar', 'foo'], {'foo': 2, 'bar': 1}),

        ('mean', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 3.0),
        ('mean', 'int', [1, 2, 3, 4, 5], 3.0),
        ('mean', 'bool', [True, False, True, False], 0.5),

        ('size', 'bool', [True, False], 2),
        ('size', 'float', [1.0, 2.0], 2),
        ('size', 'int', [1, 2], 2),
        ('size', 'str', ['foo', 'bar'], 2),

        ('sum', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 15.0),
        ('sum', 'int', [1, 2, 3, 4, 5], 15),
        ('sum', 'bool', [True, False, True], 2,),

        ('to_list', 'bool', [True, False], [True, False]),
        ('to_list', 'float', [1.0, 2.0], [1.0, 2.0]),
        ('to_list', 'int', [1, 2], [1, 2]),
        ('to_list', 'str', ['foo', 'bar'], ['foo', 'bar']),
    ],
)
def test_methods_no_arg(
    test_method: str,
    dtype: str,
    nums: LIST_TYPE,
    expected_value: RESULT,
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
        ('__getitem__', 'str', ['foo', 'bar', 'baz'], 'foo', {'index': 0}),

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
        ('get', 'str', ['foo', 'bar', 'baz'], 'foo', {'index': 0}),

        ('union_all', 'bool', [True, False], [True, False, False, True], {
         'other': ul.from_seq([False, True], dtype='bool')}),
        ('union_all', 'float', [1.0, 2.0], [1.0, 2.0, 3.0, 4.0], {
         'other': ul.from_seq([3.0, 4.0], dtype='float')}),
        ('union_all', 'int', [1, 2], [1, 2, 3, 4], {
         'other': ul.from_seq([3, 4], dtype='int')}),
        ('union_all', 'str', ['foo', 'bar'], ['foo', 'bar', 'baz', 'zoo'], {
         'other': ul.from_seq(['baz', 'zoo'], dtype='str')}),

        ('var', 'bool', [True, False], 0.25, {}),
        ('var', 'bool', [True, True, True, False], 0.25, {"ddof": 1}),
        ('var', 'float', [1.0, 2.0, 3.0, 4.0], 1.25, {}),
        ('var', 'float', [1.0, 2.0, 3.0], 1.0, {"ddof": 1}),
        ('var', 'int', [1, 2, 3, 4], 1.25, {}),
        ('var', 'int', [1, 2, 3], 1.0, {"ddof": 1}),
    ],
)
def test_methods_with_args(
    test_method: str,
    dtype: str,
    nums: LIST_TYPE,
    expected_value: RESULT,
    kwargs: dict,
) -> None:
    arr = ul.from_seq(nums, dtype)
    result = getattr(arr, test_method)(**kwargs)
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        ('__setitem__', 'bool', [True, False], [
            True, True], {'index': 1, 'elem': True}),
        ('__setitem__', 'float', [1.0, 2.0], [
         1.0, 3.0], {'index': 1, 'elem': 3.0}),
        ('__setitem__', 'int', [1, 2], [1, 3], {'index': 1, 'elem': 3}),
        ('__setitem__', 'str', ['foo', 'bar'], [
         'foo', 'baz'], {'index': 1, 'elem': 'baz'}),

        ('append', 'bool', [True], [True, False], {'elem': False}),
        ('append', 'float', [1.0], [1.0, 2.0], {'elem': 2.0}),
        ('append', 'int', [1], [1, 2], {'elem': 2}),
        ('append', 'str', ['foo'], ['foo', 'bar'], {'elem': 'bar'}),

        ('pop', 'bool', [True, False], [True], {}),
        ('pop', 'float', [1.0, 2.0], [1.0], {}),
        ('pop', 'int', [1, 2], [1], {}),
        ('pop', 'str', ['foo', 'bar'], ['foo'], {}),

        ('set', 'bool', [True, False], [
         True, True], {'index': 1, 'elem': True}),
        ('set', 'float', [1.0, 2.0], [1.0, 3.0], {'index': 1, 'elem': 3.0}),
        ('set', 'int', [1, 2], [1, 3], {'index': 1, 'elem': 3}),
        ('set', 'str', ['foo', 'bar'], [
         'foo', 'baz'], {'index': 1, 'elem': 'baz'}),
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
        ('bool', [True, False], [True, True], {'index': 1, 'elem': True}),
        ('float', [1.0, 2.0], [1.0, 3.0], {'index': 1, 'elem': 3.0}),
        ('int', [1, 2], [1, 3], {'index': 1, 'elem': 3}),
        ('str', ['foo', 'bar'], ['foo', 'baz'], {'index': 1, 'elem': 'baz'}),
    ],
)
def test_indexing_operations(
    dtype: str,
    nums: LIST_TYPE,
    expected_value: LIST_TYPE,
    kwargs: dict,
) -> None:
    index = kwargs["index"]
    elem = kwargs["elem"]
    # Set
    test_method = "set-item"
    arr = ul.from_seq(nums, dtype)
    arr[index] = elem
    check_test_result(dtype, test_method, arr, expected_value)

    # Get
    test_method = "get-item"
    expected_value = kwargs["elem"]
    result = arr[index]
    check_test_result(dtype, test_method, result, expected_value)


@pytest.mark.parametrize(
    "dtype, nums, expected_value, expected_dtype",
    [
        ('bool', [True, False], [1, 0], 'int'),
        ('bool', [True, False], [1.0, 0.0], 'float'),
        ('bool', [True, False], [True, False], 'bool'),
        ('bool', [True, False], ['true', 'false'], 'str'),

        ('float', [1.0, 2.0], [1, 2], 'int'),
        ('float', [1.0, 2.0], [1.0, 2.0], 'float'),
        ('float', [-1.0, 0.0, 1.0, 2.0], [True, False, True, True], 'bool'),
        ('float', [1.0, 1.1], ['1.0', '1.1'], 'str'),

        ('int', [1, 2], [1, 2], 'int'),
        ('int', [1, 2], [1.0, 2.0], 'float'),
        ('int', [-1, 0, 1, 2], [True, False, True, True], 'bool'),
        ('int', [1, 2], ['1', '2'], 'str'),

        ('str', ['1', '2'], [1, 2], 'int'),
        ('str', ['1.0', '2.0'], [1.0, 2.0], 'float'),
        ('str', ['true', 'false'], [True, False], 'bool'),
        ('str', ['foo', 'bar'], ['foo', 'bar'], 'str'),
    ],
)
def test_astype(
    dtype: str,
    nums: LIST_TYPE,
    expected_value: LIST_TYPE,
    expected_dtype: str,
) -> None:
    """
    The output of `astype` is already tested in `test_methods_with_args`.
    We run additional tests here:
        - The astype method should return a new ulist object;
        - The returned object should has correct dtype;
        - The returned object should has correct values;
        - If the returned object is not a BooleanList,  then it can be
          casted back to `arr`.
    """
    # Type conversion
    arr = ul.from_seq(nums, dtype=dtype)
    result = arr.astype(expected_dtype)
    test_method = f"astype {expected_dtype}"
    check_test_result(dtype, test_method, result, expected_value)
    assert result.dtype == expected_dtype
    assert id(result) != id(arr)

    # Cast back to origin type
    if result.dtype != "bool":
        arr1 = result.astype(dtype)
        test_method = f"Cast back {dtype}"
        check_test_result(expected_dtype, test_method, arr1, arr.to_list())
