from ulist.utils import Benchmarker, BenchmarkScore, MAX_DTYPE_LEN, MAX_ITEM_LEN
from typing import Any

import pytest


def test_benchmark_score() -> None:
    # Test scores when win
    bench = BenchmarkScore(
        name='foo',
        dtype='int',
        _scores={
            100: 0.9,
            1000: 1.0,
            10000: 1.1,
            100000: 1.2,
            1000000: 1.3,
        }
    )

    expected: Any = ['foo', 'int', '0.9x', '1.0x',
                     '1.1x', '1.2x', '1.3x', '1.1x', 'Y']
    assert bench.scores == expected

    # Test scores when lose
    bench = BenchmarkScore(
        name='foo',
        dtype='int',
        _scores={
            100: 0.1,
            1000: 0.1,
            10000: 0.1,
            100000: 0.2,
            1000000: 0.5,
        }
    )
    expected = ['foo', 'int', '0.1x', '0.1x',
                '0.1x', '0.2x', '0.5x', '0.2x', 'N']
    assert bench.scores == expected

    # Test header
    assert bench._header == [
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

    # Test _as_markdown

    cell_sizes = [max(6, len(x) + 2) for x in bench._header]
    cell_sizes[0] = MAX_ITEM_LEN
    cell_sizes[1] = MAX_DTYPE_LEN
    expected = "| Item           | Dtype  | XS   | S    | M    " + \
        "| L    | XL   | Average | Faster |"
    assert bench._as_markdown(bench._header, cell_sizes) == expected

    # Test _line
    line = bench._line(cell_sizes)
    expected = ['--------------', '------', '----', '----',
                '----', '----', '----', '-------', '------']
    assert line == expected

    # Test display
    bench.display(True)
    bench.display(False)


def _test_bench_marker(bench_marker: Benchmarker):
    bench = bench_marker(debug=True)
    bench.n_runs = (1, 1, 1, 1, 1)
    bench.run()


class _Int(Benchmarker):
    def cases(self) -> list:
        return [
            ([0], 1),
            ([0], 1),
            ([0], 1),
            ([0], 1),
            ([0], 1),
        ]

    def ulist_fn(self, args) -> None:
        pass

    def other_fn(self, args) -> None:
        pass


class _Float(Benchmarker):
    def cases(self) -> list:
        return [
            ([0.0],),
            ([0.0],),
            ([0.0],),
            ([0.0],),
            ([0.0],),
        ]

    def ulist_fn(self, args) -> None:
        pass

    def other_fn(self, args) -> None:
        pass


class _Bool(Benchmarker):
    def cases(self) -> list:
        return [
            ([True],),
            ([True],),
            ([True],),
            ([True],),
            ([True],),
        ]

    def ulist_fn(self, args) -> None:
        pass

    def other_fn(self, args) -> None:
        pass


class _String(Benchmarker):
    def cases(self) -> list:
        return [
            (['a'],),
            (['a'],),
            (['a'],),
            (['a'],),
            (['a'],),
        ]

    def ulist_fn(self, args) -> None:
        pass

    def other_fn(self, args) -> None:
        pass


@pytest.mark.parametrize(
    "test_class",
    [
        _Int,
        _Float,
        _Bool,
        _String,
    ],
)
def test_bench_marker(test_class: Benchmarker) -> None:
    _test_bench_marker(test_class)
