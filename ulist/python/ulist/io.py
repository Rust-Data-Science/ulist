from __future__ import annotations  # To avoid circular import.
from .ulist import read_csv as _read_csv
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:  # To avoid circular import.
    from . import UltraFastList


def read_csv(path: str, schema: Dict[str, str]) -> Dict[str, UltraFastList]:
    """Read the csv file.

    Args:
        path (str):
            The path of the csv file.
        schema (Dict[str,str]):
            The structure of the csv file, such as
            `{"foo" : "int", "bar" : "bool"}`

    Returns:
        Dict[str, UltraFastList]
    """
    from . import UltraFastList  # To avoid circular import.
    schema_seq = [x for x in schema.items()]  # To ensure the right order
    rslist = [UltraFastList(x) for x in _read_csv(path, schema_seq)]
    res = {}
    for i in range(len(schema_seq)):
        res[schema_seq[i][0]] = rslist[i]
    return res
