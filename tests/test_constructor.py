from typing import Callable, List

import pytest
import ulist as ul
from ulist.utils import check_test_result


@pytest.mark.parametrize(
    "test_method, args, kwargs, expected_value",
    [
        (ul.arange, (3,), {}, [0, 1, 2],),
        (ul.arange, (0, 3,), {}, [0, 1, 2],),
        (ul.arange, (0, 4, 2,), {}, [0, 2],),
        (ul.arange, (0, 5, 2,), {}, [0, 2, 4],),
        (ul.arange, (), {"start": 3}, [0, 1, 2],),
        (ul.arange, (), {"start": 0, "stop": 3}, [0, 1, 2],),
        (ul.arange, (), {"start": 5, "step": 2}, [0, 2, 4],),
        (ul.arange, (), {"start": 0, "stop": 5, "step": 2}, [0, 2, 4],),
        (ul.arange, (5,), {"step": 2}, [0, 2, 4],),
        (ul.arange, (0,), {"stop": 5, "step": 2}, [0, 2, 4],),

        (ul.from_seq, (range(3), "int"), {}, [0, 1, 2],),
        (ul.from_seq, (range(3), "float"), {}, [0.0, 1.0, 2.0],),
        (ul.from_seq, ([False, True], "bool"), {}, [False, True],),
        (ul.from_seq, ([0, 1, 2], "int"), {}, [0, 1, 2],),
        (ul.from_seq, ((0, 1, 2), "int"), {}, [0, 1, 2],),
    ],
)
def test_constructors(
    test_method: Callable,
    args: tuple,
    kwargs: dict,
    expected_value: List[bool],
):
    result = test_method(*args, **kwargs)
    if type(expected_value[0]) == int:
        dtype = "int"
    elif type(expected_value[0]) == float:
        dtype = "float"
    elif type(expected_value[0]) == bool:
        dtype = "bool"
    else:
        raise TypeError(f"Unexpected type {type(expected_value[0])}!")
    check_test_result(dtype, test_method, result, expected_value)
