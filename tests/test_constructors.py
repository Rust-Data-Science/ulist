from typing import Callable, List, Optional

import pytest
import ulist as ul
from ulist.utils import check_test_result


@pytest.mark.parametrize(
    "test_method, args, kwargs, expected_value",
    [
        (ul.arange, (3,), {}, [0, 1, 2],),
        (ul.arange, (3,), {"dtype": "int"}, [0, 1, 2],),
        (ul.arange, (3,), {"dtype": "int32"}, [0, 1, 2],),
        (ul.arange, (3,), {"dtype": "int64"}, [0, 1, 2],),

        (ul.arange, (0, 3,), {}, [0, 1, 2],),
        (ul.arange, (0, 4, 2,), {}, [0, 2],),
        (ul.arange, (0, 5, 2,), {}, [0, 2, 4],),
        (ul.arange, (), {"start": 3}, [0, 1, 2],),
        (ul.arange, (), {"start": 0, "stop": 3}, [0, 1, 2],),
        (ul.arange, (), {"start": 5, "step": 2}, [0, 2, 4],),
        (ul.arange, (), {"start": 0, "stop": 5, "step": 2}, [0, 2, 4],),
        (ul.arange, (5,), {"step": 2}, [0, 2, 4],),
        (ul.arange, (0,), {"stop": 5, "step": 2}, [0, 2, 4],),

        (ul.repeat, (0, 3), {}, [0, 0, 0],),
        (ul.repeat, (1.0, 3), {}, [1.0, 1.0, 1.0],),
        (ul.repeat, (False, 3), {}, [False, False, False],),
        (ul.repeat, ('foo', 3), {}, ['foo', 'foo', 'foo'],),

        (ul.from_seq, (range(3), "float"), {}, [0.0, 1.0, 2.0],),
        (ul.from_seq, (range(3), "int"), {}, [0, 1, 2],),
        (ul.from_seq, (range(3), "int32"), {}, [0, 1, 2],),
        (ul.from_seq, (range(3), "int64"), {}, [0, 1, 2],),

        (ul.from_seq, ([False, True], "bool"), {}, [False, True],),
        (ul.from_seq, ([0.0, 1.0, 2.0], "float"), {}, [0.0, 1.0, 2.0],),
        (ul.from_seq, ([0, 1, 2], "int"), {}, [0, 1, 2],),
        (ul.from_seq, (['foo', 'bar'], "string"), {}, ['foo', 'bar'],),

        (ul.from_seq, ((False, True), "bool"), {}, [False, True],),
        (ul.from_seq, ((0.0, 1.0, 2.0), "float"), {}, [0.0, 1.0, 2.0],),
        (ul.from_seq, ((0, 1, 2), "int"), {}, [0, 1, 2],),
        (ul.from_seq, (('foo', 'bar'), "string"), {}, ['foo', 'bar'],),
        (ul.from_seq, (('foo', 'bar', None), "string"),
         {}, ['foo', 'bar', None],),

        (ul.cycle, (range(3), 1, 'float'), {}, [0.0],),
        (ul.cycle, (range(3), 1, 'int32'), {}, [0],),
        (ul.cycle, (range(3), 1, 'int64'), {}, [0],),
        (ul.cycle, (range(3), 1, 'int'), {}, [0],),
        (ul.cycle, (range(3), 2, 'int'), {}, [0, 1],),
        (ul.cycle, (range(3), 3, 'int'), {}, [0, 1, 2],),
        (ul.cycle, (range(3), 4, 'int'), {}, [0, 1, 2, 0],),
        (ul.cycle, (range(3), 5, 'int'), {}, [0, 1, 2, 0, 1],),
        (ul.cycle, (range(3), 6, 'int'), {}, [0, 1, 2, 0, 1, 2],),

        (ul.cycle, ([True, False], 3, 'bool'), {}, [True, False, True],),
        (ul.cycle, ([0.0, 1.0], 3, 'float'), {}, [0.0, 1.0, 0.0],),
        (ul.cycle, ([0, 1], 3, 'int'), {}, [0, 1, 0],),
        (ul.cycle, (['foo', 'bar'], 3, 'string'), {}, ['foo', 'bar', 'foo'],),

        (ul.cycle, ((True, False), 3, 'bool'), {}, [True, False, True],),
        (ul.cycle, ((0.0, 1.0), 3, 'float'), {}, [0.0, 1.0, 0.0],),
        (ul.cycle, ((0, 1), 3, 'int'), {}, [0, 1, 0],),
        (ul.cycle, (('foo', 'bar'), 3, 'string'), {}, ['foo', 'bar', 'foo'],),
    ],
)
def test_constructors(
    test_method: Callable,
    args: tuple,
    kwargs: dict,
    expected_value: List[Optional[bool]],
) -> None:
    result = test_method(*args, **kwargs)
    if type(expected_value[0]) == int:
        dtype = "int"
    elif type(expected_value[0]) == float:
        dtype = "float"
    elif type(expected_value[0]) == bool:
        dtype = "bool"
    elif type(expected_value[0]) == str:
        dtype = "string"
    else:
        raise TypeError(f"Unexpected type {type(expected_value[0])}!")
    check_test_result(dtype, test_method, result, expected_value)
