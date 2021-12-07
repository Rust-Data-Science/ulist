import pytest
import ulist as ul
from typing import Union, List

NUM_TYPE = Union[float, int]
LIST_TYPE = Union[List[float], List[int]]


@pytest.mark.parametrize(
    "dtype, nums",
    [
        ("float", [1, 0]),
        ("int", [1, 0]),
        ("bool", [True, False]),
    ],
)
@pytest.mark.parametrize(
    "test_method, expected_value",
    [
        ("copy", [1, 0]),
        ("to_list", [1, 0]),
        ("size", 2),
    ],
)
def test(
    dtype: str,
    nums: List[NUM_TYPE],
    test_method: str,
    expected_value: LIST_TYPE,
):
    arr = ul.from_iter(nums, dtype)
    result = getattr(arr, test_method)()
    if hasattr(result, "to_list"):
        result = result.to_list()
    msg = (
        f"dtype - {dtype}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    assert result == expected_value, msg
