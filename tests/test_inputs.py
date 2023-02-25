from pathlib import Path
from typing import Callable, Dict, List

import pytest
from ulist.utils import check_test_result

import ulist as ul

here = Path(__file__).parent.resolve()


@pytest.mark.parametrize(
    "test_method, args, kwargs, expected_value",
    [
        (ul.read_csv, (), {
            "path": str(here / "test_csv/00_test_int.csv"),
            "schema": {"int32": "int32", "int64": "int64"}
        }, {
            "int32": [-2147483648, 2147483647, +2147483647],
            "int64": [-9223372036854774808,
                      9223372036854774807,
                      +9223372036854774807],
        }),
        (ul.read_csv, (), {
            "path": str(here / "test_csv/01_test_float.csv"),
            "schema": {"float32": "float32", "float64": "float64"}
        }, {
            # Precision problem in float32
            "float32": [3.14159, 0.314, 0.314],
            "float64": [3.14159, 31.4, 31.4]
        }),
        (ul.read_csv, (), {
            "path": str(here / "test_csv/02_test_bool.csv"),
            "schema": {"bool": "bool"}
        }, {
            "bool": [True, False, True, False]
        }),
        (ul.read_csv, (), {
            "path": str(here / "test_csv/03_test_string.csv"),
            "schema": {"string": "string"}
        }, {
            "string": ["String", 'Hello, "World"', None, "Long\nString"]
        }),
        (ul.read_csv, (), {
            "path": str(here / "test_csv/04_test_nan.csv"),
            "schema": {"int": "int",
                       "float": "float",
                       "string": "string",
                       "bool": "bool"}
        }, {
            "int": [None, 2, 3, 4],
            "float": [1.0, None, 3.0, 4.0],
            "string": ["1", "2", None, "4"],
            "bool": [True, False, True, None]
        }),
        (ul.read_csv, (), {  # schema.len() < field.len()
            "path": str(here / "test_csv/04_test_nan.csv"),
            "schema": {"int": "int",
                       "bool": "bool"}
        }, {
            "int": [None, 2, 3, 4],
            "bool": [True, False, True, None]
        }),
        (ul.read_csv, (), {  # schema.len() > field.len()
            "path": str(here / "test_csv/02_test_bool.csv"),
            "schema": {"foo": "int",
                       "bar": "bool",
                       "bool": "bool"}
        }, {
            "foo": [],
            "bar": [],
            "bool": [True, False, True, False]
        })
    ],
)
def test_constructors(
    test_method: Callable,
    args: tuple,
    kwargs: dict,
    expected_value: Dict[str, List]
) -> None:
    result = test_method(*args, **kwargs)
    check_test_result(kwargs["path"], test_method, result, expected_value)
