from __future__ import annotations  # To avoid circular import.
from .ulist import read_csv as _read_csv
from typing import Callable, List, TYPE_CHECKING

if TYPE_CHECKING:  # To avoid circular import.
    from . import UltraFastList


def read_csv() -> List[UltraFastList]:
    from . import UltraFastList  # To avoid circular import.
    return [UltraFastList(x) for x in _read_csv()]
