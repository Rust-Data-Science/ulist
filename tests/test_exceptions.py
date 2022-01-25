from typing import Callable, Type

import pytest
import ulist as ul

_ARR = ul.from_seq(range(3), dtype='int')
_ARR._values = [0, 1, 2]  # type: ignore


@pytest.mark.parametrize(
    "test_method, kwargs, expected_error",
    [
        (
            _ARR._arithmetic_method,
            {
                "other": None, "fn": _ARR.add, "fn_scala": _ARR.add_scala
            },
            TypeError
        ),
        (_ARR.astype, {"dtype": "foo"}, ValueError),
        (ul.cycle, {"obj": [1, 2], "size": 3, "dtype": "foo"}, ValueError),
        (ul.from_seq, {"obj": [1, 2], "dtype": "foo"}, ValueError),
        (ul.repeat, {"elem": dict(), "size": 3}, TypeError),
        (ul.UltraFastList, {"values": [1, 2]}, TypeError),
        (_ARR.var, {}, TypeError),
    ],
)
def test_exceptions(
    test_method: Callable,
    kwargs: dict,
    expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        test_method(**kwargs)
