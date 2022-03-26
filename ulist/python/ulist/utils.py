from abc import ABC, abstractmethod
from dataclasses import dataclass
from timeit import timeit
from typing import Any, Callable, Dict, List, Sequence, Tuple, Union

import ulist as ul

from .typedef import COUNTER, ELEM, LIST_PY

MAX_ITEM_LEN = 16
MAX_DTYPE_LEN = 8


def expand_dtypes(func: Callable) -> Callable:
    """
    Generate test cases for `int32` and `int64` dtypes by copying the
    test cases of `int` dtype.
    """
    def _new_arg(s: str) -> tuple:
        return tuple([x if x != s else s for x in arg])

    result = []
    for arg in func.pytestmark[0].args[1]:
        if 'int' in arg:
            arg_int64 = _new_arg('int64')
            result.append(arg_int64)
    for arg in result:
        func.pytestmark[0].args[1].append(arg)
    return func


def compare_dtypes(dtype1: str, dtype2: str) -> bool:
    """Compare two dtypes with each other."""
    if dtype2 == 'int':
        dtype2, dtype1 = dtype1, dtype2
    if dtype1 == 'int':
        return dtype2 in ('int', 'int64')
    return dtype1 == dtype2


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
    if hasattr(result, "to_list"):
        result = result.to_list()  # type: ignore
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
    _scores: dict

    @property
    def scores(self) -> List[str]:
        """For the score schema please refer to `self._header` method."""
        result = [self.name, self.dtype]
        for v in self._scores.values():
            result.append(str(v) + 'x')
        avg = round(sum(self._scores.values()) / len(self._scores), 1)
        result.append(str(avg) + 'x')
        if avg > 1:
            result.append('Y')
        else:
            result.append('N')
        return result

    def _as_markdown(self, text: List[str], cell_sizes: List[int]) -> str:
        result = ['|']
        for t, cell_size in zip(text, cell_sizes):
            content = [' '] * cell_size
            for i in range(cell_size):
                if i == 0:
                    continue
                if i - 1 < len(t):
                    content[i] = t[i - 1]
            result.append("".join(content))
            result.append('|')
        return "".join(result)

    def _line(self, cell_sizes: List[int]) -> List[str]:
        return ['-' * (x - 2) for x in cell_sizes]

    @property
    def _header(self) -> List[str]:
        return [
            'Item',
            'Dtype',
            'XS',
            'S',
            'M',
            'L',
            'XL',
            'Average',
            'Faster'
        ]

    def display(self, show_header: bool = True) -> None:
        """
        Display the benchmark score as a markdown table similar to below:

        --------
        | Item     | Dtype | XS   | S    | M    | L    | XL   | Average |
        | -------  | ------| ---- | ---- | ---- | ---- | ---- | ------- |
        | AddOne   | int   | 0.9x | 1.0x | 1.0x | 1.0x | 1.1x | 1.0x    |
        | ArraySum | int   | 4.8x | 6.2x | 7.4x | 6.4x | 7.3x | 6.4x    |
        | EqualOne | int   | 1.3x | 1.3x | 1.0x | 0.9x | 0.8x | 1.1x    |

        Item - The task to compare the performances.
        Dtype - The array element type.
        Sample Vol. - See `Benchmarker`.

        Take the 3rd line for example, it means by running the task
        EqualOne with dtype=int, the ulist's speed is 1.1 times of numpy
        on average.
        """
        cell_sizes = [max(6, len(x) + 2) for x in self._header]
        cell_sizes[0] = MAX_ITEM_LEN
        cell_sizes[1] = MAX_DTYPE_LEN

        if show_header:
            print(self._as_markdown(self._header, cell_sizes))
            line = self._line(cell_sizes)
            print(self._as_markdown(line, cell_sizes))

        print((self._as_markdown(self.scores, cell_sizes)))


class Benchmarker(ABC):
    """
    An abstract class for comparing the performance between `ulist` and other
    framework such as `numpy`.

    There are 5 rounds for the task with different array sizes and number of
    runs:
        XS - array size 100, run 100K times;
        S - array size 1K, run 100K times;
        M - array size 10K, run 10K times;
        L - array size 100K, run 1K times;
        XL - array size 1M, run 100 times.

    and the result of each round and the average result are both recorded.

    The abstract methods need to be overridden by subclass. The tuples in the
    list returned store the input of each round test. The first element of the
    tuple should be a list with corresponding size, and the other elements of
    the tuple should be scalars if needed.

    Examples
    --------
    >>> class AllIsTrue(Benchmarker):
    ...    def cases(self) -> list:
    ...        return [
    ...            ([True for _ in range(100)],),
    ...            ([True for _ in range(1000)],),
    ...            ([True for _ in range(10000)],),
    ...            ([True for _ in range(100000)],),
    ...            ([True for _ in range(1000000)],),
    ...        ]

    ...    def ulist_fn(self, args) -> None:
    ...        args[0].all()

    ...    def other_fn(self, args) -> None:
    ...        args[0].all()
    """

    def __init__(self, debug: bool = False) -> None:
        super().__init__()
        self.debug = debug
        self.n_runs = (100000, 100000, 10000, 1000, 100)
        self.sizes = (100, 1000, 10000, 100000, 1000000)
        assert len(self.n_runs) == len(self.cases())
        if not self.debug:
            assert all(x == len(y[0])
                       for x, y in zip(self.sizes, self.cases()))
        assert len(self.dtype()) < MAX_DTYPE_LEN
        assert len(self.__class__.__name__) < MAX_ITEM_LEN

    @abstractmethod
    def cases(self) -> List[Tuple[Any, ...]]:
        """Benchmark cases for each round."""

    def other_constructor(self, arr: list):
        if self.debug:
            return None
        import numpy as np  # type: ignore
        if isinstance(arr[0], int):
            dtype = "int32"
        elif isinstance(arr[0], float):
            dtype = "float32"
        elif isinstance(arr[0], bool):
            dtype = "bool"
        elif isinstance(arr[0], str):
            dtype = "str"
        else:
            raise TypeError(f"Invalid type {type(arr[0])}!")
        return np.array(arr, dtype=dtype)

    @abstractmethod
    def ulist_fn(self, args: Sequence[Any]) -> None:
        """The ulist function to benchmark."""

    @abstractmethod
    def other_fn(self, args: Sequence[Any]) -> None:
        """The numpy function to benchmark."""

    def dtype(self) -> str:
        """Return the dtype for the constructors."""
        element_type = str(type(self.cases()[0][0][0]))
        left = element_type.index("'") + 1
        right = element_type.rindex("'")
        result = element_type[left: right]
        if result == 'str':
            return 'string'
        return result

    def run(self) -> BenchmarkScore:
        """Run the benchmarking task."""
        ulist_time_elapsed = self._run(self.ulist_fn)
        other_time_elapsed = self._run(self.other_fn)
        scores = dict()
        for k, v in ulist_time_elapsed.items():
            scores[k] = round(other_time_elapsed[k] / v, 1)
        return BenchmarkScore(
            name=type(self).__name__,
            dtype=self.dtype(),
            _scores=scores,
        )

    def _run(self, fn: Callable) -> Dict[int, float]:
        if fn == self.ulist_fn:
            constructor: Callable = lambda x: ul.from_seq(
                x, dtype=self.dtype())
        else:
            constructor = self.other_constructor
        result = dict()
        for n_run, size, args in zip(self.n_runs, self.sizes, self.cases()):
            _args = self._process_args(args, constructor)
            result[size] = timeit(lambda: fn(_args), number=n_run)
        return result

    def _process_args(
        self,
        args: Sequence[Any],
        constructor: Callable
    ) -> list:
        result = []
        for arg in args:
            if isinstance(arg, list):
                result.append(constructor(arg))
            else:
                result.append(arg)
        return result
