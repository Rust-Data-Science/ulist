from typing import Dict, List, Union, Optional

from .ulist import (
    BooleanList,
    FloatList32,
    FloatList64,
    IntegerList32,
    IntegerList64,
    StringList
)

ELEM = Union[int, float, bool, str]
ELEM_OPT = Union[Optional[int], Optional[float], Optional[bool], Optional[str]]
NUM = Union[int, float]
LIST_PY = Union[List[float], List[int], List[bool], List[str]]
LIST_RS = Union[FloatList32, FloatList64, IntegerList32,
                IntegerList64, BooleanList, StringList]
NUM_LIST_RS = Union[FloatList32, FloatList64, IntegerList32, IntegerList64]
COUNTER = Union[Dict[int, int], Dict[bool, int], Dict[str, int]]
