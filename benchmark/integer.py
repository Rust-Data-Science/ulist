from random import randint, seed

import numpy as np
from ulist.utils import Benchmarker

seed(100)


class AddOne(Benchmarker):
    def cases(self) -> list:
        return [
            (list(range(100)),),
            (list(range(1000)),),
            (list(range(10000)),),
            (list(range(100000)),),
            (list(range(1000000)),),
        ]

    def ulist_fn(self, args) -> None:
        args[0] + 1

    def other_fn(self, args) -> None:
        args[0] + 1


class ArraySum(Benchmarker):
    def cases(self) -> list:
        return [
            ([randint(1, 10) for _ in range(100)],),
            ([randint(1, 10) for _ in range(1000)],),
            ([randint(1, 10) for _ in range(10000)],),
            ([randint(1, 10) for _ in range(100000)],),
            ([randint(1, 10) for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0].sum()

    def other_fn(self, args) -> None:
        args[0].sum()


class EqualOne(Benchmarker):
    def cases(self) -> list:
        return [
            ([randint(1, 10) for _ in range(100)],),
            ([randint(1, 10) for _ in range(1000)],),
            ([randint(1, 10) for _ in range(10000)],),
            ([randint(1, 10) for _ in range(100000)],),
            ([randint(1, 10) for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0] == 1

    def other_fn(self, args) -> None:
        args[0] == 1


class Max(Benchmarker):
    def cases(self) -> list:
        return [
            ([x for x in range(100)],),
            ([x for x in range(1000)],),
            ([x for x in range(10000)],),
            ([x for x in range(100000)],),
            ([x for x in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0].max()

    def other_fn(self, args) -> None:
        args[0].max()


class MulTwo(Benchmarker):
    def cases(self) -> list:
        return [
            ([x for x in range(100)],),
            ([x for x in range(1000)],),
            ([x for x in range(10000)],),
            ([x for x in range(100000)],),
            ([x for x in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0] * 2

    def other_fn(self, args) -> None:
        args[0] * 2


class UniqueElem(Benchmarker):
    def cases(self) -> list:
        return [
            ([randint(1, 10) for _ in range(100)],),
            ([randint(1, 10) for _ in range(1000)],),
            ([randint(1, 10) for _ in range(10000)],),
            ([randint(1, 10) for _ in range(100000)],),
            ([randint(1, 10) for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0].unique()

    def other_fn(self, args) -> None:
        np.unique(args[0])


class Sort(Benchmarker):
    def cases(self) -> list:
        return [
            ([randint(1, 100) for _ in range(100)],),
            ([randint(1, 1000) for _ in range(1000)],),
            ([randint(1, 10000) for _ in range(10000)],),
            ([randint(1, 100000) for _ in range(100000)],),
            ([randint(1, 1000000) for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0].sort(ascending=True)

    def other_fn(self, args) -> None:
        np.sort(args[0])
