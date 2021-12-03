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

    fn _new(vec: Vec<T>) -> Self;

    fn _operate(&'a self, other: &'a Self, func: impl Fn(T, T) -> T) -> Self {
        let vec = self
            .values()
            .iter()
            .zip(other.values().iter())
            .map(|(x, y)| func(*x, *y))
            .collect();
        List::_new(vec)
    }

    fn _operate_scala(&'a self, func: impl Fn(T) -> T) -> Self {
        let vec = self.values().iter().map(|x| func(*x)).collect();
        List::_new(vec)
    }

    fn _sort(&self, vec: &mut Vec<T>, ascending: bool);

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
        let vec = self
            .values()
            .iter()
            .zip(condition._values.iter())
            .filter(|(_, y)| **y)
            .map(|(x, _)| *x)
            .collect();
        List::_new(vec)
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
        self.values().len()
    }

    fn sort(&'a self, ascending: bool) -> Self {
        let mut vec = self.to_list();
        let mut _vec = &mut vec;
        self._sort(_vec, ascending);
        List::_new(vec)
    }

    fn sub(&'a self, other: &'a Self) -> Self {
        self._operate(other, |x, y| x - y)
    }

    fn sub_scala(&'a self, num: T) -> Self {
        self._operate_scala(|x| x - num)
    }

    fn sum(&'a self) -> T {
        self.values().iter().sum()
    }

    fn to_list(&'a self) -> Vec<T> {
        self.values().clone()
    }

    fn unique(&'a self) -> Self {
        let mut vec = self.to_list();
        self._sort(&mut vec, true);
        vec.dedup();
        List::_new(vec)
    }

    fn values(&'a self) -> &'a Vec<T>;
}

/// List for bool.
#[pyclass]
pub struct BooleanList {
    _values: Vec<bool>,
}

#[pymethods]
impl BooleanList {
    #[new]
    fn new(vec: Vec<bool>) -> Self {
        BooleanList { _values: vec }
    }
}
