
from typing import List, Sequence, Union, Optional

import pytest
import ulist as ul
from ulist.utils import check_test_result


@pytest.mark.parametrize(
    "test_method, nums, expected_value",
    [
        ('__repr__', [1, 2], 'IndexList([1, 2])'),
        ('__repr__', range(0, 100), 'IndexList([0, 1, 2, ..., 97, 98, 99])'),

        ('__str__', [1, 2], '[1, 2]'),
        ('__str__', range(0, 100), '[0, 1, 2, ..., 97, 98, 99]'),

        ('back', [1, 2, 5], 5),

        ('to_list', [1, 2], [1, 2]),
    ],
)
def test_methods(
    test_method: str,
    nums: Sequence[int],
    expected_value: Union[Optional[int], List[Optional[int]]],
) -> None:
    dtype = 'IndexList'
    arr = ul.IndexList(nums)
    result = getattr(arr, test_method)()
    if hasattr(result, 'to_list'):
        result = result.to_list()
    check_test_result(dtype, test_method, result, expected_value)
