use crate::base::List;
use crate::boolean::BooleanList;
use num::traits::pow::pow;
use num::traits::AsPrimitive;
use num::One;
use std::cmp::PartialEq;
use std::cmp::PartialOrd;
use std::ops::Add;
use std::ops::Div;
use std::ops::Fn;
use std::ops::Mul;
use std::ops::Sub;

/// Abstract List with Numerical type elements.
pub trait NumericalList<T>: List<T>
where
    T: AsPrimitive<f32>
        + PartialEq
        + PartialOrd
        + Add<Output = T>
        + Sub<Output = T>
        + Mul<Output = T>
        + Div<Output = T>
        + One,
{
    // Arrange the following methods in alphabetical order.
    fn _operate(&self, other: &Self, func: impl Fn(T, T) -> T) -> Self {
        let vec = self
            .values()
            .iter()
            .zip(other.values().iter())
            .map(|(&x, &y)| func(x, y))
            .collect();
        List::_new(vec)
    }

    fn _operate_scala<U>(&self, func: impl Fn(T) -> U) -> Vec<U> {
        self.values().iter().map(|&x| func(x)).collect()
    }

    fn _sort(&self, vec: &mut Vec<T>, ascending: bool);

    fn add(&self, other: &Self) -> Self {
        self._operate(other, |x, y| x + y)
    }

    fn add_scala(&self, num: T) -> Self {
        List::_new(self._operate_scala(|x| x + num))
    }

    fn div(&self, other: &Self) -> Vec<f32>;

    fn div_scala(&self, num: f32) -> Vec<f32>;

    fn filter(&self, condition: &BooleanList) -> Self {
        let vec = self
            .values()
            .iter()
            .zip(condition.values().iter())
            .filter(|(_, y)| **y)
            .map(|(x, _)| *x)
            .collect();
        List::_new(vec)
    }

    fn greater_than_scala(&self, num: T) -> BooleanList {
        BooleanList::new(self._operate_scala(|x| x > num))
    }

    fn less_than_scala(&self, num: T) -> BooleanList {
        BooleanList::new(self._operate_scala(|x| x < num))
    }

    fn max(&self) -> T;

    fn mean(&self) -> f32 {
        let numeritor: f32 = self.sum().as_();
        let denominator: f32 = self.size().as_();
        numeritor / denominator
    }

    fn min(&self) -> T;

    fn mul(&self, other: &Self) -> Self {
        self._operate(other, |x, y| x * y)
    }

    fn mul_scala(&self, num: T) -> Self {
        List::_new(self._operate_scala(|x| x * num))
    }

    fn pow_scala(&self, num: usize) -> Self {
        List::_new(self._operate_scala(|x| pow(x, num)))
    }

    fn sort(&self, ascending: bool) -> Self {
        let mut vec = self.to_list();
        let mut _vec = &mut vec;
        self._sort(_vec, ascending);
        List::_new(vec)
    }

    fn sub(&self, other: &Self) -> Self {
        self._operate(other, |x, y| x - y)
    }

    fn sub_scala(&self, num: T) -> Self {
        List::_new(self._operate_scala(|x| x - num))
    }

    // There is no elegant way to implement the sum method here, and have to
    // duplicate the codes in IntegerList and FloatList for the time being.
    fn sum(&self) -> T;

    fn unique(&self) -> Self {
        let mut vec = self.to_list();
        self._sort(&mut vec, true);
        vec.dedup();
        List::_new(vec)
    }
}
