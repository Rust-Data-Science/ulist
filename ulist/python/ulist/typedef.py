from typing import List, Union, Dict

from .ulist import BooleanList, FloatList, IntegerList, StringList

ELEM = Union[int, float, bool, str]
NUM = Union[int, float]
LIST_PY = Union[List[float], List[int], List[bool], List[str]]
LIST_RS = Union[FloatList, IntegerList, BooleanList, StringList]
NUM_LIST_RS = Union[FloatList, IntegerList]
COUNTER = Union[Dict[int, int], Dict[bool, int], Dict[str, int]]
