from ulist.utils import BenchmarkScore, Benchmarker
import ulist as ul
import numpy as np



class ArraySum(Benchmarker):
    def cases(self) -> list:
        return [
            ([1],),
            ([1] * 10,),
            ([1] * 100,),
            ([1] * 1000,),
            ([1] * 10000,),
            ([1] * 100000,),
            ([1] * 1000000,),
        ]

    def other_constructor(self, arr: list):
        return np.array(arr, dtype=int)

    def ulist_fn(self, args) -> None:
        args[0].sum()

    def other_fn(self, args) -> None:
        args[0].sum()

    def dtype(self) -> str:
        return "int"
