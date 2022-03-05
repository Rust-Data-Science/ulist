from random import choice, seed

from ulist.utils import Benchmarker

seed(100)


class AllIsTrue(Benchmarker):
    def cases(self) -> list:
        return [
            ([True for _ in range(100)],),
            ([True for _ in range(1000)],),
            ([True for _ in range(10000)],),
            ([True for _ in range(100000)],),
            ([True for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0].all()

    def other_fn(self, args) -> None:
        args[0].all()


class AndOp(Benchmarker):
    def cases(self) -> list:
        return [
            ([choice([False, True]) for _ in range(100)],),
            ([choice([False, True]) for _ in range(1000)],),
            ([choice([False, True]) for _ in range(10000)],),
            ([choice([False, True]) for _ in range(100000)],),
            ([choice([False, True]) for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0] & args[0]

    def other_fn(self, args) -> None:
        args[0] & args[0]


class AnyIsTrue(Benchmarker):
    def cases(self) -> list:
        return [
            ([False for _ in range(100)],),
            ([False for _ in range(1000)],),
            ([False for _ in range(10000)],),
            ([False for _ in range(100000)],),
            ([False for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0].any()

    def other_fn(self, args) -> None:
        args[0].any()


class NotOp(Benchmarker):
    def cases(self) -> list:
        return [
            ([choice([False, True]) for _ in range(100)],),
            ([choice([False, True]) for _ in range(1000)],),
            ([choice([False, True]) for _ in range(10000)],),
            ([choice([False, True]) for _ in range(100000)],),
            ([choice([False, True]) for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        ~(args[0])

    def other_fn(self, args) -> None:
        ~(args[0])


class OrOp(Benchmarker):
    def cases(self) -> list:
        return [
            ([choice([False, True]) for _ in range(100)],),
            ([choice([False, True]) for _ in range(1000)],),
            ([choice([False, True]) for _ in range(10000)],),
            ([choice([False, True]) for _ in range(100000)],),
            ([choice([False, True]) for _ in range(1000000)],),
        ]

    def ulist_fn(self, args) -> None:
        args[0] | args[0]

    def other_fn(self, args) -> None:
        args[0] | args[0]
