use crate::base::List;
use crate::base::_fill_na;
use crate::boolean::BooleanList;
use std::ops::Add;
use std::ops::Div;
use std::ops::Fn;
use std::ops::Mul;
use std::ops::Sub;

/// Abstract List with Numerical type elements.
pub trait NumericalList<T, U, V>: List<T>
where
    T: Copy + PartialOrd + Add<Output = T> + Sub<Output = T> + Mul<Output = T> + Div<Output = T>,
{
    // Arrange the following methods in alphabetical order.
    fn _fn_num<W: Clone>(&self, func: impl Fn(T) -> W, default: W) -> Vec<W> {
        let mut vec = self.values().iter().map(|&x| func(x)).collect();
        _fill_na(&mut vec, self.na_indexes(), default);
        vec
    }

    fn _fn(&self, other: &Self, func: impl Fn(T, T) -> T) -> Self {
        let mut vec = self
            .values()
            .iter()
            .zip(other.values().iter())
            .map(|(&x, &y)| func(x, y))
            .collect();
        _fill_na(&mut vec, self.na_indexes(), self.na_value());
        let hset = self.na_indexes().clone();
        List::_new(vec, hset)
    }

    fn add(&self, other: &Self) -> Self {
        self._fn(other, |x, y| x + y)
    }

    fn add_scala(&self, elem: T) -> Self {
        let hset = self.na_indexes().clone();
        List::_new(self._fn_num(|x| x + elem, self.na_value()), hset)
    }

    fn argmax(&self) -> usize;

    fn argmin(&self) -> usize;

    fn div(&self, other: &Self) -> Vec<V>;

    fn div_scala(&self, elem: V) -> Vec<V>;

    fn greater_than_or_equal_scala(&self, elem: T) -> BooleanList {
        let hset = self.na_indexes().clone();
        BooleanList::new(self._fn_num(|x| x >= elem, false), hset)
    }

    fn greater_than_scala(&self, elem: T) -> BooleanList {
        let hset = self.na_indexes().clone();
        BooleanList::new(self._fn_num(|x| x > elem, false), hset)
    }

    fn less_than_or_equal_scala(&self, elem: T) -> BooleanList {
        let hset = self.na_indexes().clone();
        BooleanList::new(self._fn_num(|x| x <= elem, false), hset)
    }

    fn less_than_scala(&self, elem: T) -> BooleanList {
        let hset = self.na_indexes().clone();
        BooleanList::new(self._fn_num(|x| x < elem, false), hset)
    }

    fn max(&self) -> T;

    fn min(&self) -> T;

    fn mul(&self, other: &Self) -> Self {
        self._fn(other, |x, y| x * y)
    }

    fn mul_scala(&self, elem: T) -> Self {
        let hset = self.na_indexes().clone();
        List::_new(self._fn_num(|x| x * elem, self.na_value()), hset)
    }

    fn pow_scala(&self, elem: U) -> Self;

    fn sub(&self, other: &Self) -> Self {
        self._fn(other, |x, y| x - y)
    }

    fn sub_scala(&self, elem: T) -> Self {
        let hset = self.na_indexes().clone();
        List::_new(self._fn_num(|x| x - elem, self.na_value()), hset)
    }

    // There is no elegant way to implement the sum method here, and have to
    // duplicate the codes in IntegerList and FloatList for the time being.
    fn sum(&self) -> T;
}
