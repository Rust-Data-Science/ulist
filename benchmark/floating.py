from random import random, seed

import numpy as np
from ulist.utils import Benchmarker

seed(100)


class AddOne(Benchmarker):
    def cases(self) -> list:
        return [
            ([float(x) for x in range(100)],),
            ([float(x) for x in range(1000)],),
            ([float(x) for x in range(10000)],),
            ([float(x) for x in range(100000)],),
            ([float(x) for x in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0] + 1.0

    def other_fn(self, args) -> None:
        args[0] + 1.0


class ArraySum(Benchmarker):
    def cases(self) -> list:
        return [
            ([random() for _ in range(100)],),
            ([random() for _ in range(1000)],),
            ([random() for _ in range(10000)],),
            ([random() for _ in range(100000)],),
            ([random() for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0].sum()

    def other_fn(self, args) -> None:
        args[0].sum()


class LessThanOne(Benchmarker):
    def cases(self) -> list:
        return [
            ([random() * 2 for _ in range(100)],),
            ([random() * 2 for _ in range(1000)],),
            ([random() * 2 for _ in range(10000)],),
            ([random() * 2 for _ in range(100000)],),
            ([random() * 2 for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0] < 1

    def other_fn(self, args) -> None:
        args[0] < 1


class Max(Benchmarker):
    def cases(self) -> list:
        return [
            ([float(x) for x in range(100)],),
            ([float(x) for x in range(1000)],),
            ([float(x) for x in range(10000)],),
            ([float(x) for x in range(100000)],),
            ([float(x) for x in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0].max()

    def other_fn(self, args) -> None:
        args[0].max()


class MulTwo(Benchmarker):
    def cases(self) -> list:
        return [
            ([float(x) for x in range(100)],),
            ([float(x) for x in range(1000)],),
            ([float(x) for x in range(10000)],),
            ([float(x) for x in range(100000)],),
            ([float(x) for x in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0] * 2.0

    def other_fn(self, args) -> None:
        args[0] * 2.0


class Sort(Benchmarker):
    def cases(self) -> list:
        return [
            ([random() for _ in range(100)],),
            ([random() for _ in range(1000)],),
            ([random() for _ in range(10000)],),
            ([random() for _ in range(100000)],),
            ([random() for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0].sort(ascending=True)

    def other_fn(self, args) -> None:
        np.sort(args[0])
