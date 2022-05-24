from typing import Dict, List, Union, Callable, Optional

import operator as op
import pytest
import ulist as ul
from ulist.utils import check_test_result, compare_dtypes, expand_dtypes

ELEM_TYPE = Union[Optional[float],
                  Optional[int], Optional[bool], Optional[str]]
LIST_TYPE = Union[List[Optional[float]], List[Optional[int]],
                  List[Optional[bool]], List[Optional[str]]]
COUNTER = Union[Dict[Optional[int], int], Dict[Optional[bool], int]]
RESULT = Union[ELEM_TYPE, LIST_TYPE, COUNTER]


@expand_dtypes
@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value",
    [
        ('__len__', 'bool', [True, False, True], 3),
        ('__len__', 'float', [1.0, 2.0, 3.0], 3),
        ('__len__', 'int', [1, 2, 3], 3),
        ('__len__', 'string', ['foo', 'bar', 'baz'], 3),
        ('__len__', 'string', ['foo', 'bar', None], 3),

        (
            "__repr__",
            "bool",
            [True, False] * 50,
            "UltraFastList([True, False, True, ..., False, True, False])",
        ),
        (
            '__repr__',
            'bool',
            [True, False],
            'UltraFastList([True, False])',
        ),
        (
            '__repr__',
            'float',
            [1.0, 2.0],
            'UltraFastList([1.0, 2.0])',
        ),
        (
            '__repr__',
            'float',
            range(0, 100),
            'UltraFastList([0.0, 1.0, 2.0, ..., 97.0, 98.0, 99.0])',
        ),
        (
            '__repr__',
            'int',
            [1, 2],
            'UltraFastList([1, 2])',
        ),
        (
            '__repr__',
            'int',
            range(0, 100),
            'UltraFastList([0, 1, 2, ..., 97, 98, 99])',
        ),
        (
            "__repr__",
            "string",
            ['foo', 'bar'] * 50,
            "UltraFastList(['foo', 'bar', 'foo', ..., 'bar', 'foo', 'bar'])",
        ),
        (
            '__repr__',
            'string',
            ['foo', 'bar'],
            "UltraFastList(['foo', 'bar'])",
        ),
        (
            "__repr__",
            "string",
            ['foo', None] * 50,
            "UltraFastList(['foo', None, 'foo', ..., None, 'foo', None])",
        ),
        (
            '__repr__',
            'string',
            ['foo', None],
            "UltraFastList(['foo', None])",
        ),

        (
            "__str__",
            "bool",
            [True, False] * 50,
            "[True, False, True, ..., False, True, False]",
        ),
        (
            '__str__',
            'bool',
            [True, False],
            '[True, False]',
        ),
        (
            '__str__',
            'float',
            [1.0, 2.0],
            '[1.0, 2.0]',
        ),
        (
            '__str__',
            'float',
            range(0, 100),
            '[0.0, 1.0, 2.0, ..., 97.0, 98.0, 99.0]',
        ),
        (
            '__str__',
            'int',
            [1, 2],
            '[1, 2]',
        ),
        (
            '__str__',
            'int',
            range(0, 100),
            '[0, 1, 2, ..., 97, 98, 99]',
        ),
        (
            "__str__",
            "string",
            ['foo', 'bar'] * 50,
            "['foo', 'bar', 'foo', ..., 'bar', 'foo', 'bar']",
        ),
        (
            '__str__',
            'string',
            ['foo', 'bar'],
            "['foo', 'bar']",
        ),
        (
            "__str__",
            "string",
            ['foo', None] * 50,
            "['foo', None, 'foo', ..., None, 'foo', None]",
        ),
        (
            '__str__',
            'string',
            ['foo', None],
            "['foo', None]",
        ),

        ('copy', 'bool', [True, False], [True, False]),
        ('copy', 'float', [1.0, 2.0], [1.0, 2.0]),
        ('copy', 'int', [1, 2], [1, 2]),
        ('copy', 'string', ['foo', 'bar'], ['foo', 'bar']),
        ('copy', 'string', ['foo', None], ['foo', None]),

        ('count_na', 'bool', [True, False, True], 0),
        ('count_na', 'int', [1, 0, 1], 0),
        ('count_na', 'string', ['foo', 'bar', 'foo'], 0),
        ('count_na', 'string', ['foo', None, 'foo'], 1),

        ('counter', 'bool', [True, False, True], {True: 2, False: 1}),
        ('counter', 'int', [1, 0, 1], {1: 2, 0: 1}),
        ('counter', 'string', ['foo', 'bar', 'foo'], {'foo': 2, 'bar': 1}),
        ('counter', 'string', ['foo', None, 'foo'], {'foo': 2, None: 1}),

        ('mean', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 3.0),
        ('mean', 'int', [1, 2, 3, 4, 5], 3.0),
        ('mean', 'bool', [True, False, True, False], 0.5),
        ('mean', 'bool', [True, False, True, False, None], 0.5),

        ('size', 'bool', [True, False], 2),
        ('size', 'float', [1.0, 2.0], 2),
        ('size', 'int', [1, 2], 2),
        ('size', 'string', ['foo', 'bar'], 2),
        ('size', 'string', ['foo', None], 2),

        ('sum', 'float', [1.0, 2.0, 3.0, 4.0, 5.0], 15.0),
        ('sum', 'int', [1, 2, 3, 4, 5], 15),
        ('sum', 'bool', [True, False, True], 2,),
        ('sum', 'bool', [True, None, True], 2,),

        ('to_list', 'bool', [True, False], [True, False]),
        ('to_list', 'float', [1.0, 2.0], [1.0, 2.0]),
        ('to_list', 'int', [1, 2], [1, 2]),
        ('to_list', 'string', ['foo', 'bar'], ['foo', 'bar']),
        ('to_list', 'string', ['foo', None], ['foo', None]),
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


@expand_dtypes
@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        ('__getitem__', 'bool', [True, False, True], True, {'index': 2}),
        ('__getitem__', 'float', [1.0, 2.0, 3.0], 2.0, {'index': 1}),
        ('__getitem__', 'int', [1, 2, 3], 1, {'index': 0}),
        ('__getitem__', 'string', ['foo', 'bar', 'baz'], 'foo', {'index': 0}),
        ('__getitem__', 'string', ['foo', None, 'baz'], 'foo', {'index': 0}),
        ('__getitem__', 'string', ['foo', None, 'baz'], None, {'index': 1}),

        ('__getitem__', 'bool', [True, False, True],
         [True, True], {'index': ul.IndexList([0, 2])}),
        ('__getitem__', 'float', [1.0, 2.0, 3.0], [1.0, 3.0],
         {'index': ul.IndexList([0, 2])}),
        ('__getitem__', 'int', [1, 2, 3],
         [1, 3], {'index': ul.IndexList([0, 2])}),
        ('__getitem__', 'string', ['foo', 'bar', 'baz'],
         ['foo', 'baz'], {'index': ul.IndexList([0, 2])}),

        ("all_equal", 'bool', [True, False], True, {"other": [True, False]}),
        ("all_equal", 'bool', [True, False], False, {"other": [True, True]}),
        ("all_equal", 'bool', [True, False], False, {"other": [False, True]}),
        ("all_equal", 'bool', [True, False], False, {"other": [False, False]}),
        ("all_equal", 'bool', [True, False], False, {"other": [True, None]}),
        ("all_equal", 'bool', [True, None], False, {"other": [True, None]}),
        ("all_equal", 'bool', [True, None], False, {"other": [True, False]}),
        ("all_equal", 'bool', [True, False], False, {"other": [True]}),
        ("all_equal", 'bool', [True, False], False, {"other": [None]}),
        ("all_equal", 'float', [1.0, 0.0], True, {"other": [1.0, 0.0]}),
        ("all_equal", 'float', [1.0, 0.0], False, {"other": [1.0, 1.0]}),
        ("all_equal", 'int', [1, 0], True, {"other": [1, 0]}),
        ("all_equal", 'int', [1, 0], False, {"other": [1, 1]}),
        ("all_equal", 'string', ['foo', 'bar'],
         True, {"other": ['foo', 'bar']}),
        ("all_equal", 'string', ['foo', 'bar'],
         False, {"other": ['foo', 'foo']}),

        ("apply", "bool", [True, False], [
         False, True], {"fn": lambda x: x == False},),  # noqa: E712
        ("apply", "float", [1.0, 2.0], [
         True, False], {"fn": lambda x: x < 2.0},),
        ("apply", "int", [1, 2], [3, 5], {"fn": lambda x: x * 2 + 1},),
        ("apply", "string", ['foo', 'bar'], [
         True, False], {"fn": lambda x: x != 'bar'},),
        ("apply", "string", ['foo', 'bar', None], [
         True, False, True], {"fn": lambda x: x != 'bar'},),

        ("equal_scala", 'bool', [True, False], [False, True], {"elem": False}),
        ("equal_scala", 'float', [1.0, 2.0, 3.0],
         [False, True, False], {"elem": 2.0}),
        ("equal_scala", 'int', [1, 2, 3], [False, True, False], {"elem": 2}),
        ("equal_scala", 'string', ['foo', 'bar'],
         [False, True], {"elem": 'bar'}),
        ("equal_scala", 'string', ['foo', 'bar', None],
         [False, True, False], {"elem": 'bar'}),

        (
            "filter",
            "bool",
            [True, True, False],
            [True, False],
            {"condition": ul.from_seq([True, False, True], 'bool')},
        ),
        (
            "filter",
            "float",
            [1.0, 2.0, 3.0],
            [1.0, 3.0],
            {"condition": ul.from_seq([True, False, True], 'bool')},
        ),
        (
            "filter",
            "int",
            [1, 2, 3],
            [1, 3],
            {"condition": ul.from_seq([True, False, True], 'bool')},
        ),
        (
            "filter",
            "string",
            ['foo', 'bar', 'baz'],
            ['foo', 'baz'],
            {"condition": ul.from_seq([True, False, True], 'bool')},
        ),
        (
            "filter",
            "string",
            ['foo', 'bar', None, None],
            ['foo', None],
            {"condition": ul.from_seq([True, False, True, False], 'bool')},
        ),

        ('get', 'bool', [True, False, True], True, {'index': 2}),
        ('get', 'float', [1.0, 2.0, 3.0], 2.0, {'index': 1}),
        ('get', 'int', [1, 2, 3], 1, {'index': 0}),
        ('get', 'string', ['foo', 'bar', 'baz'], 'foo', {'index': 0}),
        ('get', 'string', ['foo', 'bar', None], 'foo', {'index': 0}),
        ('get', 'string', ['foo', 'bar', None], None, {'index': 2}),

        ('get_by_indexes', 'bool', [True, False, True],
         [True, True], {'indexes': ul.IndexList([0, 2])}),
        ('get_by_indexes', 'float', [1.0, 2.0, 3.0], [1.0, 3.0],
         {'indexes': ul.IndexList([0, 2])}),
        ('get_by_indexes', 'int', [1, 2, 3],
         [1, 3], {'indexes': ul.IndexList([0, 2])}),
        ('get_by_indexes', 'string', ['foo', 'bar', 'baz'],
         ['foo', 'baz'], {'indexes': ul.IndexList([0, 2])}),
        ('get_by_indexes', 'string', ['foo', 'bar', None],
         ['foo', None], {'indexes': ul.IndexList([0, 2])}),

        ("not_equal_scala", 'bool', [False, True, False], [
         True, False, True], {"elem": True}),
        ("not_equal_scala", 'float', [1.0, 2.0, 3.0], [
         True, False, True], {"elem": 2.0}),
        ("not_equal_scala", 'int', [1, 2, 3],
         [True, False, True], {"elem": 2}),
        ("not_equal_scala", 'string', ['foo', 'bar', 'baz'],
         [True, False, True], {"elem": 'bar'}),
        ("not_equal_scala", 'string', ['foo', 'bar', None],
         [True, False, True], {"elem": 'bar'}),

        ('union_all', 'bool', [True, False], [True, False, False, True], {
         'other': ul.from_seq([False, True], dtype='bool')}),
        ('union_all', 'float', [1.0, 2.0], [1.0, 2.0, 3.0, 4.0], {
         'other': ul.from_seq([3.0, 4.0], dtype='float')}),
        ('union_all', 'int', [1, 2], [1, 2, 3, 4], {
         'other': ul.from_seq([3, 4], dtype='int')}),
        ('union_all', 'string', ['foo', 'bar'], ['foo', 'bar', 'baz', 'zoo'], {
         'other': ul.from_seq(['baz', 'zoo'], dtype='string')}),
        ('union_all', 'string', ['foo', 'bar'], ['foo', 'bar', 'baz', None], {
         'other': ul.from_seq(['baz', None], dtype='string')}),

        ('var', 'bool', [True, False], 0.25, {}),
        ('var', 'bool', [True, True, True, False], 0.25, {"ddof": 1}),
        ('var', 'float', [1.0, 2.0, 3.0, 4.0], 1.25, {}),
        ('var', 'float', [1.0, 2.0, 3.0], 1.0, {"ddof": 1}),
        ('var', 'int', [1, 2, 3, 4], 1.25, {}),
        ('var', 'int', [1, 2, 3], 1.0, {"ddof": 1}),
        ('var', 'int', [1, 2, 3, None], 1.0, {"ddof": 1}),

        ("where", "bool", [True, True, False, False], [
         False, False], {"fn": lambda x: x == False},),  # noqa: E712
        ("where", "float", [1.0, 2.0, 3.0, 4.0], [
         1.0, 2.0], {"fn": lambda x: x < 3.0},),
        ("where", "int", [1, 2, 3, 4], [
            3, 4], {"fn": lambda x: x > 2},),
        ("where", "string", ['foo', 'bar', 'baz'], [
            'foo', 'baz'], {"fn": lambda x: x != 'bar'},),
        ("where", "string", ['foo', 'bar', 'baz', None], [
            'foo', 'baz', None], {"fn": lambda x: x != 'bar'},),
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
    fn = getattr(arr, test_method)
    if kwargs.get("other") and isinstance(kwargs["other"], list):
        result = fn(ul.from_seq(kwargs["other"], dtype))
    else:
        result = fn(**kwargs)
    check_test_result(dtype, test_method, result, expected_value)


@expand_dtypes
@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        ('__setitem__', 'bool', [True, False], [
            True, True], {'index': 1, 'elem': True}),
        ('__setitem__', 'float', [1.0, 2.0], [
         1.0, 3.0], {'index': 1, 'elem': 3.0}),
        ('__setitem__', 'int', [1, 2], [1, 3], {'index': 1, 'elem': 3}),
        ('__setitem__', 'string', ['foo', 'bar'], [
         'foo', 'baz'], {'index': 1, 'elem': 'baz'}),

        ('append', 'bool', [True], [True, False], {'elem': False}),
        ('append', 'float', [1.0], [1.0, 2.0], {'elem': 2.0}),
        ('append', 'int', [1], [1, 2], {'elem': 2}),
        ('append', 'string', ['foo'], ['foo', 'bar'], {'elem': 'bar'}),

        ('pop', 'bool', [True, False], [True], {}),
        ('pop', 'float', [1.0, 2.0], [1.0], {}),
        ('pop', 'int', [1, 2], [1], {}),
        ('pop', 'string', ['foo', 'bar'], ['foo'], {}),

        ('set', 'bool', [True, False], [
         True, True], {'index': 1, 'elem': True}),
        ('set', 'float', [1.0, 2.0], [1.0, 3.0], {'index': 1, 'elem': 3.0}),
        ('set', 'int', [1, 2], [1, 3], {'index': 1, 'elem': 3}),
        ('set', 'string', ['foo', 'bar'], [
         'foo', 'baz'], {'index': 1, 'elem': 'baz'}),

        ('replace', 'bool', [True, False, True], [
         False, False, False], {'old': True, 'new': False}),
        ('replace', 'float', [1.0, 0.0, 1.0], [
         0.0, 0.0, 0.0], {'old': 1.0, 'new': 0.0}),
        ('replace', 'int', [1, 0, 1], [0, 0, 0], {'old': 1, 'new': 0}),
        ('replace', 'string', ['foo', 'bar', 'foo'], [
         'bar', 'bar', 'bar'], {'old': 'foo', 'new': 'bar'}),

        (
            'sort',
            'bool',
            [True, False, True],
            [False, True, True],
            {'ascending': True}
        ),
        (
            'sort',
            'bool',
            [True, False, True],
            [True, True, False],
            {'ascending': False}
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
            'sort',
            'string',
            ['foo', 'bar', 'baz'],
            ['bar', 'baz', 'foo'],
            {'ascending': True}
        ),
        (
            'sort',
            'string',
            ['foo', 'bar', 'baz'],
            ['foo', 'baz', 'bar'],
            {'ascending': False}
        ),

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


@expand_dtypes
@pytest.mark.parametrize(
    "dtype, nums, expected_value, kwargs",
    [
        ('bool', [True, False], [True, True], {'index': 1, 'elem': True}),
        ('float', [1.0, 2.0], [1.0, 3.0], {'index': 1, 'elem': 3.0}),
        ('int', [1, 2], [1, 3], {'index': 1, 'elem': 3}),
        ('string', ['foo', 'bar'], ['foo', 'baz'],
         {'index': 1, 'elem': 'baz'}),
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


@expand_dtypes
@pytest.mark.parametrize(
    "dtype, nums, expected_value, expected_dtype",
    [
        ('bool', [True, False], [1, 0], 'int'),
        ('bool', [True, False], [1.0, 0.0], 'float'),
        ('bool', [True, False], [True, False], 'bool'),
        ('bool', [True, False], ['true', 'false'], 'string'),

        ('float', [1.0, 2.0], [1, 2], 'int'),
        ('float', [1.0, 2.0], [1.0, 2.0], 'float'),
        ('float', [-1.0, 0.0, 1.0, 2.0], [True, False, True, True], 'bool'),
        ('float', [1.0, 1.1], ['1.0', '1.1'], 'string'),

        ('int', [1, 2], [1, 2], 'int'),
        ('int', [1, 2], [1.0, 2.0], 'float'),
        ('int', [-1, 0, 1, 2], [True, False, True, True], 'bool'),
        ('int', [1, 2], ['1', '2'], 'string'),

        ('string', ['1', '2'], [1, 2], 'int'),
        ('string', ['1.0', '2.0'], [1.0, 2.0], 'float'),
        ('string', ['true', 'false'], [True, False], 'bool'),
        ('string', ['foo', 'bar'], ['foo', 'bar'], 'string'),
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
    assert compare_dtypes(result.dtype, expected_dtype)
    assert id(result) != id(arr)

    # Cast back to origin type
    if result.dtype != "bool":
        arr1 = result.astype(dtype)
        test_method = f"Cast back {dtype}"
        check_test_result(expected_dtype, test_method, arr1, arr.to_list())


@expand_dtypes
@pytest.mark.parametrize(
    "test_method, dtype, nums, expected_value, kwargs",
    [
        (op.eq, 'bool', [True, False], [False, True], {"other": False}),
        (op.eq, 'float', [1.0, 2.0, 3.0], [
         False, True, False], {"other": 2.0}),
        (op.eq, 'int', [1, 2, 3], [False, True, False], {"other": 2}),
        (op.eq, 'string', ['foo', 'bar'], [False, True], {"other": 'bar'}),

        (op.ne, 'bool', [False, True, False],
         [True, False, True], {"other": True}),
        (op.ne, 'float', [1.0, 2.0, 3.0], [True, False, True], {"other": 2.0}),
        (op.ne, 'int', [1, 2, 3], [True, False, True], {"other": 2}),
        (op.ne, 'string', ['foo', 'bar', 'baz'],
         [True, False, True], {"other": 'bar'}),
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


@expand_dtypes
@pytest.mark.parametrize(
    "dtype, nums, expected_value",
    [
        (
            'bool',
            [True, False, True, False, True],
            [False, True],
        ),
        (
            'float',
            [5.0, 3.0, 2.0, 4.0, 1.0, 3.0],
            [1.0, 2.0, 3.0, 4.0, 5.0],
        ),
        (
            'int',
            [5, 3, 2, 4, 1, 3],
            [1, 2, 3, 4, 5],
        ),
        (
            'string',
            ['foo', 'bar', 'foo'],
            ['bar', 'foo'],
        ),
    ],
)
def test_unique(
    dtype: str,
    nums: LIST_TYPE,
    expected_value: RESULT,
) -> None:
    test_method = "unique"
    arr = ul.from_seq(nums, dtype)
    result = getattr(arr, test_method)()
    result.sort(True)
    check_test_result(dtype, test_method, result, expected_value)
