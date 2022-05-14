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
LIST_PY = Union[List[Optional[float]], List[Optional[int]],
                List[Optional[bool]], List[Optional[str]]]
LIST_RS = Union[FloatList32, FloatList64, IntegerList32,
                IntegerList64, BooleanList, StringList]
NUM_LIST_RS = Union[FloatList32, FloatList64, IntegerList32, IntegerList64]
COUNTER = Union[
    Dict[Optional[int], int],
    Dict[Optional[bool], int],
    Dict[Optional[str], int],
]
