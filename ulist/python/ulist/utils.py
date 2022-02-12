from abc import ABC, abstractmethod
from dataclasses import dataclass
from timeit import timeit
from typing import Callable, Dict, List, Tuple, Union

import ulist as ul

from .typedef import COUNTER, ELEM, LIST_PY


def check_test_result(
    dtype: str,
    test_method: Union[Callable, str],
    result: Union[ELEM, LIST_PY, ul.UltraFastList],
    expected_value: Union[ELEM, LIST_PY, COUNTER],
):
    """Test if the result is as expected. Both value and type.
    Args:
        dtype (str): 'int', 'float' or 'bool'.
        test_method (Union[Callable, str]): A method name or a function.
        result (Union[ELEM, LIST_PY, ul.UltraFastList])
        expected_value (Union[ELEM, LIST_PY])
    """
    msg = (
        f"dtype - {dtype}"
        + f" test_method - {test_method}"
        + f" result - {result}"
        + f" expected - {expected_value}"
    )
    if isinstance(result, ul.UltraFastList):
        result = result.to_list()
    if isinstance(result, list) and \
            isinstance(expected_value, list):
        assert len(result) == len(expected_value), msg
        for x, y in zip(result, expected_value):
            assert type(x) == type(y) and x == y, msg
    elif isinstance(result, dict) and \
            isinstance(expected_value, dict):
        for key in result.keys():
            x = result[key]
            y = result[key]
            assert type(x) == type(y) and x == y
        assert len(result) == len(expected_value)
    else:
        assert type(result) == type(expected_value), msg
        assert result == expected_value, msg


@dataclass
class BenchmarkScore:
    name: str
    dtype: str
    scores: dict


class Benchmarker(ABC):
    def __init__(
        self,
        n_runs: Union[int, Tuple[int, ...]] = 1000,
        sizes: Tuple[int, ...] = (1, 10, 100, 1000, 10000, 100000, 1000000)
    ) -> None:
        super().__init__()
        if isinstance(n_runs, int):
            n_runs = tuple([n_runs] * len(sizes))
        else:
            assert len(n_runs) == len(sizes)
        assert len(n_runs) == len(self.cases())
        assert all(x == len(y[0]) for x, y in zip(sizes, self.cases()))
        self.n_runs = n_runs
        self.sizes = sizes

    @abstractmethod
    def cases(self) -> list:
        pass

    @abstractmethod
    def ulist_fn(self, args) -> None:
        pass

    @abstractmethod
    def other_fn(self, args) -> None:
        pass

    @abstractmethod
    def dtype(self, args) -> str:
        pass

    def run(self) -> BenchmarkScore:
        ulist_time_elapsed = self._run(self.ulist_fn)
        other_time_elapsed = self._run(self.other_fn)
        scores = {
            k: other_time_elapsed[k] / v for k, v in ulist_time_elapsed}
        return BenchmarkScore(
            name=type(self).__name__,
            dtype=self.dtype(),
            scores=scores,
        )

    def _run(self, fn: Callable) -> Dict[int, float]:
        result = dict()
        for n_run, size, args in zip(self.n_runs, self.sizes, self.cases()):
            result[size] = timeit(fn(args), number=n_run)
        return result
