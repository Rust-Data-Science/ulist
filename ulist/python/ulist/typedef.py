from typing import List, Union, Dict

from .ulist import BooleanList, FloatList, IntegerList

ELEM = Union[int, float, bool]
NUM = Union[int, float]
LIST_PY = Union[List[float], List[int], List[bool]]
NUM_LIST_PY = Union[List[float], List[int]]
LIST_RS = Union[FloatList, IntegerList, BooleanList]
NUM_LIST_RS = Union[FloatList, IntegerList]
NUM_OR_LIST = Union[NUM, NUM_LIST_RS]
COUNTER = Union[Dict[int, int], Dict[bool, int]]
