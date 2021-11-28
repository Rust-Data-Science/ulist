use num::traits::pow::pow;
use num::traits::AsPrimitive;
use num::One;
use pyo3::prelude::*;
use std::cmp::PartialEq;
use std::iter::Sum;
use std::marker::Sized;
use std::ops::Add;
use std::ops::Div;
use std::ops::Fn;
use std::ops::Mul;
use std::ops::Sub;

/// An abstract List.
pub trait List<'a, T>
where
    T: AsPrimitive<f32>
        + Sum<&'a T>
        + PartialEq
        + Add<Output = T>
        + Sub<Output = T>
        + Mul<Output = T>
        + Div<Output = T>
        + One,
    Self: Sized,
{
    // Arrange the following methods in alphabetical order.

    fn _new(list: Vec<T>) -> Self;

    fn _operate(&'a self, other: &'a Self, func: impl Fn(T, T) -> T) -> Self {
        let list = self
            ._values()
            .iter()
            .zip(other._values().iter())
            .map(|(x, y)| func(*x, *y))
            .collect();
        List::_new(list)
    }

    fn _operate_scala(&'a self, func: impl Fn(T) -> T) -> Self {
        let list = self._values().iter().map(|x| func(*x)).collect();
        List::_new(list)
    }

    fn _sort(&self, list: &mut Vec<T>, ascending: bool);

    fn _values(&'a self) -> &'a Vec<T>;

    fn add(&'a self, other: &'a Self) -> Self {
        self._operate(other, |x, y| x + y)
    }

    fn add_scala(&'a self, num: T) -> Self {
        self._operate_scala(|x| x + num)
    }

    fn copy(&'a self) -> Self {
        List::_new(self.to_list())
    }

    fn div(&'a self, other: &'a Self) -> Vec<f32>;

    fn div_scala(&'a self, num: f32) -> Vec<f32>;

    fn filter(&'a self, condition: &BooleanList) -> Self {
        let list = self
            ._values()
            .iter()
            .zip(condition._list.iter())
            .filter(|(_, y)| **y)
            .map(|(x, _)| *x)
            .collect();
        List::_new(list)
    }

    fn max(&'a self) -> T;

    fn mean(&'a self) -> f32 {
        let numeritor: f32 = self.sum().as_();
        let denominator: f32 = self.size().as_();
        numeritor / denominator
    }

    fn min(&'a self) -> T;

    fn mul(&'a self, other: &'a Self) -> Self {
        self._operate(other, |x, y| x * y)
    }

    fn mul_scala(&'a self, num: T) -> Self {
        self._operate_scala(|x| x * num)
    }

    fn pow_scala(&'a self, num: usize) -> Self {
        self._operate_scala(|x| pow(x, num))
    }

    fn size(&'a self) -> usize {
        self._values().len()
    }

    fn sort(&'a self, ascending: bool) -> Self {
        let mut list = self.to_list();
        let mut _list = &mut list;
        self._sort(_list, ascending);
        List::_new(list)
    }

    fn sub(&'a self, other: &'a Self) -> Self {
        self._operate(other, |x, y| x - y)
    }

    fn sub_scala(&'a self, num: T) -> Self {
        self._operate_scala(|x| x - num)
    }

    fn sum(&'a self) -> T {
        self._values().iter().sum()
    }

    fn to_list(&'a self) -> Vec<T> {
        self._values().clone()
    }

    fn unique(&'a self) -> Self {
        let mut list = self.to_list();
        self._sort(&mut list, true);
        list.dedup();
        List::_new(list)
    }
}

/// List for bool.
#[pyclass]
pub struct BooleanList {
    _list: Vec<bool>,
}

#[pymethods]
impl BooleanList {
    #[new]
    fn new(list: Vec<bool>) -> Self {
        BooleanList { _list: list }
    }
}
