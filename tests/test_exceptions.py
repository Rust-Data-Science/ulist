from typing import Callable, Type

import pytest
import ulist as ul

_ARR1 = ul.from_seq(range(3), dtype='int')
_ARR1._values = [0, 1, 2]  # type: ignore
_ARR2 = ul.from_seq([], dtype='int')
_ARR3 = ul.from_seq([None, None], dtype='int')


class _Foo:
    pass


@pytest.mark.parametrize(
    "test_method, kwargs, expected_error",
    [
        (
            _ARR2.argmax,
            {},
            RuntimeError
        ),
        (
            _ARR3.argmax,
            {},
            RuntimeError
        ),

        (
            _ARR2.argmin,
            {},
            RuntimeError
        ),
        (
            _ARR3.argmin,
            {},
            RuntimeError
        ),

        (
            _ARR1._arithmetic_method,
            {
                "other": None, "fn": _ARR1.add, "fn_scala": _ARR1.add_scala
            },
            TypeError
        ),

        (
            _ARR1.astype,
            {"dtype": "foo"},
            ValueError
        ),

        (
            ul.cycle,
            {"obj": [1, 2], "size": 3, "dtype": "foo"},
            ValueError
        ),

        (
            ul.from_seq,
            {"obj": [1, 2], "dtype": "foo"},
            ValueError
        ),

        (
            _ARR2.max,
            {},
            RuntimeError
        ),
        (
            _ARR3.max,
            {},
            RuntimeError
        ),

        (
            _ARR2.min,
            {},
            RuntimeError
        ),
        (
            _ARR3.min,
            {},
            RuntimeError
        ),

        (
            ul.repeat,
            {"elem": dict(), "size": 3},
            TypeError
        ),

        (
            ul.select,
            {
                "conditions": [
                    ul.from_seq([True, False], dtype='bool'),
                    ul.from_seq([False, False], dtype='bool')
                ],
                "choices": [1, 2],
                "default": _Foo(),
            },
            TypeError
        ),
        (
            ul.select,
            {
                "conditions": [
                    ul.from_seq([True], dtype='bool'),
                    ul.from_seq([False, False], dtype='bool')
                ],
                "choices": [1, 2],
                "default": 0,
            },
            RuntimeError
        ),
        (
            ul.select,
            {
                "conditions": [
                    ul.from_seq([True, None], dtype='bool'),
                    ul.from_seq([False, False], dtype='bool')
                ],
                "choices": [1, 2],
                "default": 0,
            },
            ValueError
        ),

        (
            ul.UltraFastList,
            {"values": [1, 2]},
            TypeError
        ),

        (
            _ARR1.var,
            {},
            TypeError
        ),

        (
            ul.from_seq([1, 2, 3], dtype='int').case(default='foo').when,
            {"fn": lambda x: x + 1, "then": "bar"},
            TypeError
        ),
        (
            ul.from_seq([1, 2, 3], dtype='int').case(default='foo').when,
            {"fn": lambda x: x < 2, "then": 1.0},
            TypeError
        ),
    ],
)
def test_exceptions(
    test_method: Callable,
    kwargs: dict,
    expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        test_method(**kwargs)
