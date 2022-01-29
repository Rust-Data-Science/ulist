from __future__ import annotations  # To avoid circular import.
from typing import TYPE_CHECKING, Callable


from .typedef import ELEM, LIST_PY, LIST_RS, NUM, NUM_OR_LIST, COUNTER
from .ulist import BooleanList, FloatList, IntegerList, StringList


if TYPE_CHECKING:  # To avoid circular import.
    from .control_flow import CaseObject


class UltraFastList:
    """
    Ultra fast list data structures written in Rust with Python bindings,
    which is abbreviated as ulist.
    """

    def __init__(self, values: LIST_RS) -> None:
        if type(values) is FloatList:
            self.dtype = "float"
        elif type(values) is IntegerList:
            self.dtype = "int"
        elif type(values) is BooleanList:
            self.dtype = "bool"
        elif type(values) is StringList:
            self.dtype = "string"
        else:
            raise TypeError(
                "Parameter values should be FloatList, "
                + "IntegerList, BooleanList or StringList type!"
            )
        self._values = values

    def __len__(self) -> int:
        """Number of elements of self."""
        return self.size()

    def _arithmetic_method(
        self, other: NUM_OR_LIST, fn: Callable, fn_scala: Callable
    ) -> "UltraFastList":
        if isinstance(other, int) or isinstance(other, float):
            return fn_scala(other)
        if type(other) is type(self):
            return fn(other)
        raise TypeError(
            "Parameter other should be int, " + "float or UltraFastList type!"
        )

    def __add__(self, other: NUM_OR_LIST) -> "UltraFastList":
        """Return self + other."""
        return self._arithmetic_method(other, self.add, self.add_scala)

    def __and__(self, other: "UltraFastList") -> "UltraFastList":
        """Return self & other."""
        return self.and_(other)

    def __eq__(self, other: int) -> "UltraFastList":  # type: ignore
        """Return self == other."""
        return self.equal_scala(other)

    def __getitem__(self, index: int) -> ELEM:
        """Return self[index]."""
        return self._values.get(index)

    def __ge__(self, other: int) -> "UltraFastList":
        """Return self >= other."""
        return self.greater_than_or_equal_scala(other)

    def __gt__(self, other: NUM) -> "UltraFastList":
        """Return self > other."""
        return self.greater_than_scala(other)

    def __invert__(self) -> "UltraFastList":
        """Return ~self."""
        return self.not_()

    def __le__(self, other: int) -> "UltraFastList":
        """Return self <= other."""
        return self.less_than_or_equal_scala(other)

    def __lt__(self, other: NUM) -> "UltraFastList":
        """Return self < other."""
        return self.less_than_scala(other)

    def __mul__(self, other: NUM_OR_LIST) -> "UltraFastList":
        """Return self * other."""
        return self._arithmetic_method(other, self.mul, self.mul_scala)

    def __ne__(self, other: int) -> "UltraFastList":  # type: ignore
        """Return self != other."""
        return self.not_equal_scala(other)

    def __or__(self, other: "UltraFastList") -> "UltraFastList":
        """Return self | other."""
        return self.or_(other)

    def __pow__(self, other: int) -> "UltraFastList":
        """Return self ** other."""
        return self._arithmetic_method(other, lambda: None, self.pow_scala)

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"UltraFastList({str(self)})"

    def __setitem__(self, index: int, elem: ELEM) -> None:
        """Set self[index] to elem."""
        self._values.set(index, elem)

    def __str__(self) -> str:
        """Return str(self)."""
        n = self.size()
        if n < 100:
            return str(self.to_list())
        if self.dtype == 'string':
            return (
                f"['{self[0]}', '{self[1]}', '{self[2]}', ..., "
                + f"'{self[n-3]}', '{self[n-2]}', '{self[n-1]}']"
            )
        return (
            f"[{self[0]}, {self[1]}, {self[2]}, ..., "
            + f"{self[n-3]}, {self[n-2]}, {self[n-1]}]"
        )

    def __sub__(self, other: NUM_OR_LIST) -> "UltraFastList":
        """Return self - other."""
        return self._arithmetic_method(other, self.sub, self.sub_scala)

    def __truediv__(self, other: NUM_OR_LIST) -> "UltraFastList":
        """Return self / other."""
        return self._arithmetic_method(other, self.div, self.div_scala)

    def add(self, other: "UltraFastList") -> "UltraFastList":
        """Return self + other."""
        assert not isinstance(self._values, (BooleanList, StringList))
        assert not isinstance(other._values, (BooleanList, StringList))
        return UltraFastList(self._values.add(other._values))

    def add_scala(self, elem: NUM) -> "UltraFastList":
        """Return self + elem."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return UltraFastList(self._values.add_scala(elem))

    def all(self) -> bool:
        """Whether all the elements of self are True."""
        assert isinstance(self._values, BooleanList)
        return self._values.all()

    def and_(self, other: "UltraFastList") -> "UltraFastList":
        """Return self & other."""
        assert isinstance(self._values, BooleanList)
        assert isinstance(other._values, BooleanList)
        return UltraFastList(self._values.and_(other._values))

    def any(self) -> bool:
        """Whether any element of self is True."""
        assert isinstance(self._values, BooleanList)
        return self._values.any()

    def append(self, elem: ELEM) -> None:
        """Adds a new element at the end of the self."""
        self._values.append(elem)

    def argmax(self) -> int:
        """Returns the indices of the maximum values of self."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return self._values.argmax()

    def argmin(self) -> int:
        """Returns the indices of the minimum values of self."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return self._values.argmin()

    def astype(self, dtype: str) -> "UltraFastList":
        """Copy of self, cast to a specified dtype.

        Raises:
            ValueError:
                Parameter dtype should be 'int', 'float', 'bool' or 'string'!

        Returns:
            UltraFastList: A ulist object.
        """
        if dtype == "int":
            if isinstance(self._values, IntegerList):
                result = self.copy()
            else:
                result = UltraFastList(self._values.as_int())
        elif dtype == "float":
            if isinstance(self._values, FloatList):
                result = self.copy()
            else:
                result = UltraFastList(self._values.as_float())
        elif dtype == "bool":
            if isinstance(self._values, BooleanList):
                result = self.copy()
            else:
                result = UltraFastList(self._values.as_bool())
        elif dtype == "string":
            if isinstance(self._values, StringList):
                result = self.copy()
            else:
                result = UltraFastList(self._values.as_str())
        else:
            raise ValueError(
                "Parameter dtype should be 'int', 'float', 'bool' or 'string'!"
            )
        return result

    def case(self, default: ELEM) -> CaseObject:
        """A method similar to SQL's `case` statement.

        Args:
            default (ELEM):
                The element inserted in output when all conditions evaluate
                to False.

        Returns:
            CaseObject

        Examples
        --------
        >>> import ulist as ul
        >>> arr = ul.arange(6)
        >>> arr
        UltraFastList([0, 1, 2, 3, 4, 5])

        >>> result = arr.case(default=2)\
        ...             .when(lambda x: x < 2, then=0)\
        ...             .when(lambda x: x < 4, then=1)\
        ...             .end()
        >>> result
        UltraFastList([0, 0, 1, 1, 2, 2])
        """
        from .control_flow import CaseObject  # To avoid circular import.
        return CaseObject(self, default=default)

    def copy(self) -> "UltraFastList":
        """Return a ulist copy of self."""
        return UltraFastList(self._values.copy())

    def counter(self) -> COUNTER:
        """
        Return a dictionary where the elements of self are stored as
        dictionary keys and their counts are stored as dictionary values.
        """
        assert not isinstance(self._values, FloatList)
        return self._values.counter()

    def div(self, other: "UltraFastList") -> "UltraFastList":
        """Return self / other."""
        assert not isinstance(self._values, (BooleanList, StringList))
        assert not isinstance(other._values, (BooleanList, StringList))
        return UltraFastList(self._values.div(other._values))

    def div_scala(self, elem: float) -> "UltraFastList":
        """Return self / elem."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return UltraFastList(self._values.div_scala(elem))

    def equal_scala(self, elem: NUM) -> "UltraFastList":
        """Return self == elem."""
        return UltraFastList(self._values.equal_scala(elem))

    def filter(self, condition: "UltraFastList") -> "UltraFastList":
        """
        According to the condition, return a ulist with elements of self
        correspondingly.
        """
        assert isinstance(condition._values, BooleanList)
        return UltraFastList(self._values.filter(condition._values))

    def get(self, index: int) -> ELEM:
        """Return self[index]."""
        return self._values.get(index)

    def greater_than_or_equal_scala(self, elem: NUM) -> "UltraFastList":
        """Return self >= elem."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return UltraFastList(self._values.greater_than_or_equal_scala(elem))

    def greater_than_scala(self, elem: NUM) -> "UltraFastList":
        """Return self > elem."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return UltraFastList(self._values.greater_than_scala(elem))

    def less_than_or_equal_scala(self, elem: NUM) -> "UltraFastList":
        """Return self <= elem."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return UltraFastList(self._values.less_than_or_equal_scala(elem))

    def less_than_scala(self, elem: NUM) -> "UltraFastList":
        """Return self < elem."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return UltraFastList(self._values.less_than_scala(elem))

    def max(self) -> NUM:
        """Return the maximum of self."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return self._values.max()

    def mean(self) -> float:
        """Return the mean of self."""
        return self.sum() / self.size()

    def min(self) -> NUM:
        """Return the minimum of self."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return self._values.min()

    def mul(self, other: "UltraFastList") -> "UltraFastList":
        """Return self * other."""
        assert not isinstance(self._values, (BooleanList, StringList))
        assert not isinstance(other._values, (BooleanList, StringList))
        return UltraFastList(self._values.mul(other._values))

    def mul_scala(self, elem: NUM) -> "UltraFastList":
        """Return self * elem."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return UltraFastList(self._values.mul_scala(elem))

    def not_(self) -> "UltraFastList":
        """Return ~self."""
        assert isinstance(self._values, BooleanList)
        return UltraFastList(self._values.not_())

    def not_equal_scala(self, elem: NUM) -> "UltraFastList":
        """Return self != elem."""
        return UltraFastList(self._values.not_equal_scala(elem))

    def or_(self, other: "UltraFastList") -> "UltraFastList":
        """Return self | other."""
        assert isinstance(self._values, BooleanList)
        assert isinstance(other._values, BooleanList)
        return UltraFastList(self._values.or_(other._values))

    def pop(self) -> None:
        """Removes the last element of self."""
        self._values.pop()

    def pow_scala(self, elem: int) -> "UltraFastList":
        """Return self ** elem."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return UltraFastList(self._values.pow_scala(elem))

    def replace(self, old: ELEM, new: ELEM) -> "UltraFastList":
        """Replace the old elements of self with the new one."""
        return UltraFastList(self._values.replace(old, new))

    def set(self, index: int, elem: ELEM) -> None:
        """Set self[index] to elem."""
        self._values.set(index, elem)

    def size(self) -> int:
        """Number of elements of self."""
        return self._values.size()

    def sort(self, ascending: bool) -> "UltraFastList":
        """Return a sorted copy of self.

        Args:
            ascending (bool):
                Ascending or descending.

        Returns:
            UltraFastList: The sorted ulist.
        """
        return UltraFastList(self._values.sort(ascending=ascending))

    def sub(self, other: "UltraFastList") -> "UltraFastList":
        """Return self - other."""
        assert not isinstance(self._values, (BooleanList, StringList))
        assert not isinstance(other._values, (BooleanList, StringList))
        return UltraFastList(self._values.sub(other._values))

    def sub_scala(self, elem: NUM) -> "UltraFastList":
        """Return self - elem."""
        assert not isinstance(self._values, (BooleanList, StringList))
        return UltraFastList(self._values.sub_scala(elem))

    def sum(self) -> NUM:
        """Return the sum of self."""
        assert not isinstance(self._values, StringList)
        return self._values.sum()

    def to_list(self) -> LIST_PY:
        """Return a list with the elements of self."""
        return self._values.to_list()

    def union_all(self, other: "UltraFastList") -> "UltraFastList":
        """Concatenate self and other together as a new ulist."""
        return UltraFastList(self._values.union_all(other._values))

    def unique(self) -> "UltraFastList":
        """Returns the sorted unique elements of self. """
        return UltraFastList(self._values.unique())

    def var(self, ddof: int = 0) -> float:
        """Returns the variance of self.

        Args:
            ddof (int, optional):
                Delta Degrees of Freedom - the divisor used in the
                calculation is N - ddof, where N represents the number
                of elements. Defaults to 0.

        Raises:
            TypeError: Only support dtype int, float and bool.

        Returns:
            float: variance
        """
        if isinstance(self._values, FloatList):
            data = self
        elif isinstance(self._values, IntegerList):
            data = self.astype('float')
        elif isinstance(self._values, BooleanList):
            data = self.astype('float')
        else:
            raise TypeError(f"Var method does not support dtype {self.dtype}!")
        mean = data.mean()
        numerator = data.sub_scala(mean).pow_scala(2).sum()
        denominator = data.size() - ddof
        return numerator / denominator

    def where(
        self,
        fn: Callable[[UltraFastList], UltraFastList]
    ) -> UltraFastList:
        """According to the function, return a ulist with elements of self
        correspondingly.

        Args:
            fn (Callable[[UltraFastList], UltraFastList]):
                Function to process self and return a BooleanList.

        Returns:
            UltraFastList: A ulist object.

        Examples
        --------
        >>> import ulist as ul
        >>> arr = ul.arange(6)
        >>> arr
        UltraFastList([0, 1, 2, 3, 4, 5])

        >>> result = arr.where(lambda x: x > 2)
        >>> result
        UltraFastList([3, 4, 5])
        """
        return self.filter(fn(self))
