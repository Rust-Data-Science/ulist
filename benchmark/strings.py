from random import choice, seed

import numpy as np
from ulist.utils import Benchmarker

seed(100)


class ContainsElem(Benchmarker):
    def cases(self) -> list:
        return [
            ([choice(['How are you?', 'I am fine!'])
             for _ in range(100)], 'fine'),
            ([choice(['How are you?', 'I am fine!'])
             for _ in range(1000)], 'fine'),
            ([choice(['How are you?', 'I am fine!'])
             for _ in range(10000)], 'fine'),
            ([choice(['How are you?', 'I am fine!'])
             for _ in range(100000)], 'fine'),
            ([choice(['How are you?', 'I am fine!'])
             for _ in range(1000000)], 'fine'),
        ]

    def ulist_fn(self, args) -> None:
        args[0].contains(args[1])

    def other_fn(self, args) -> None:
        np.char.find(args[0], args[1]) != -1


class CountElems(Benchmarker):
    def cases(self) -> list:
        return [
            ([choice(['foo', 'bar', 'baz']) for _ in range(100)], ),
            ([choice(['foo', 'bar', 'baz']) for _ in range(1000)], ),
            ([choice(['foo', 'bar', 'baz']) for _ in range(10000)], ),
            ([choice(['foo', 'bar', 'baz']) for _ in range(100000)], ),
            ([choice(['foo', 'bar', 'baz']) for _ in range(1000000)], ),
        ]

    def ulist_fn(self, args) -> None:
        args[0].counter()

    def other_fn(self, args) -> None:
        unique, counts = np.unique(args[0], return_counts=True)
        dict(zip(unique, counts))


class EqualFoo(Benchmarker):
    def cases(self) -> list:
        return [
            ([choice(['foo', 'bar', 'baz']) for _ in range(100)], ),
            ([choice(['foo', 'bar', 'baz']) for _ in range(1000)], ),
            ([choice(['foo', 'bar', 'baz']) for _ in range(10000)], ),
            ([choice(['foo', 'bar', 'baz']) for _ in range(100000)], ),
            ([choice(['foo', 'bar', 'baz']) for _ in range(1000000)], ),
        ]

    def ulist_fn(self, args) -> None:
        args[0] == 'foo'

    def other_fn(self, args) -> None:
        args[0] == 'foo'
