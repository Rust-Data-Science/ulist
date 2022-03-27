use crate::base::List;
use crate::boolean::BooleanList;
use std::ops::Add;
use std::ops::Div;
use std::ops::Fn;
use std::ops::Mul;
use std::ops::Sub;

/// Abstract List with Numerical type elements.
pub trait NumericalList<T, V, W>: List<T>
where
    T: Copy + PartialOrd + Add<Output = T> + Sub<Output = T> + Mul<Output = T> + Div<Output = T>,
{
    // Arrange the following methods in alphabetical order.
    fn _fn_num<U>(&self, func: impl Fn(T) -> U) -> Vec<U> {
        self.values().iter().map(|&x| func(x)).collect()
    }

    fn _fn(&self, other: &Self, func: impl Fn(T, T) -> T) -> Self {
        let vec = self
            .values()
            .iter()
            .zip(other.values().iter())
            .map(|(&x, &y)| func(x, y))
            .collect();
        List::_new(vec)
    }

    fn add(&self, other: &Self) -> Self {
        self._fn(other, |x, y| x + y)
    }

    fn add_scala(&self, elem: T) -> Self {
        List::_new(self._fn_num(|x| x + elem))
    }

    fn argmax(&self) -> usize;

    fn argmin(&self) -> usize;

    fn div(&self, other: &Self) -> Vec<W>;

    fn div_scala(&self, elem: W) -> Vec<W>;

    fn greater_than_or_equal_scala(&self, elem: T) -> BooleanList {
        BooleanList::new(self._fn_num(|x| x >= elem))
    }

    fn greater_than_scala(&self, elem: T) -> BooleanList {
        BooleanList::new(self._fn_num(|x| x > elem))
    }

    fn less_than_or_equal_scala(&self, elem: T) -> BooleanList {
        BooleanList::new(self._fn_num(|x| x <= elem))
    }

    fn less_than_scala(&self, elem: T) -> BooleanList {
        BooleanList::new(self._fn_num(|x| x < elem))
    }

    fn max(&self) -> T;

    fn min(&self) -> T;

    fn mul(&self, other: &Self) -> Self {
        self._fn(other, |x, y| x * y)
    }

    fn mul_scala(&self, elem: T) -> Self {
        List::_new(self._fn_num(|x| x * elem))
    }

    fn pow_scala(&self, elem: V) -> Self;

    fn sub(&self, other: &Self) -> Self {
        self._fn(other, |x, y| x - y)
    }

    fn sub_scala(&self, elem: T) -> Self {
        List::_new(self._fn_num(|x| x - elem))
    }

    // There is no elegant way to implement the sum method here, and have to
    // duplicate the codes in IntegerList and FloatList for the time being.
    fn sum(&self) -> T;
}
