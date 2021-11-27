use num::traits::AsPrimitive;
use pyo3::class::sequence::PySequenceProtocol;
use pyo3::prelude::*;
use std::cmp::PartialEq;
use std::iter::Sum;
use std::marker::Sized;

/// An abstract List.
trait List<'a, T>
where
    T: AsPrimitive<f32> + Sum<&'a T> + PartialEq,
    Self: Sized,
{
    // Arrange the following methods in alphabetical order.
    fn _new(list: Vec<T>) -> Self;

    fn _sort(&self, list: &mut Vec<T>, ascending: bool);

    fn _values(&'a self) -> &'a Vec<T>;

    fn copy(&'a self) -> Self {
        List::_new(self.to_list())
    }

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

    fn size(&'a self) -> usize {
        self._values().len()
    }

    fn sort(&'a self, ascending: bool) -> Self {
        let mut list = self.to_list();
        let mut _list = &mut list;
        self._sort(_list, ascending);
        List::_new(list)
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

/// List for f32.
#[pyclass]
struct FloatList {
    _list: Vec<f32>,
}

#[pymethods]
impl FloatList {
    #[new]
    fn new(list: Vec<f32>) -> Self {
        List::_new(list)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        List::filter(self, condition)
    }

    pub fn max(&self) -> f32 {
        List::max(self)
    }

    pub fn mean(&self) -> f32 {
        List::mean(self)
    }

    pub fn min(&self) -> f32 {
        List::min(self)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) -> Self {
        List::sort(self, ascending)
    }

    pub fn sum(&self) -> f32 {
        List::sum(self)
    }

    pub fn to_list(&self) -> Vec<f32> {
        List::to_list(self)
    }

    pub fn unique(&self) -> Self {
        List::unique(self)
    }
}

impl<'a> List<'a, f32> for FloatList {
    fn _new(list: Vec<f32>) -> Self {
        Self { _list: list }
    }

    fn _sort(&self, list: &mut Vec<f32>, ascending: bool) {
        if ascending {
            list.sort_by(|a, b| a.partial_cmp(b).unwrap());
        } else {
            list.sort_by(|a, b| b.partial_cmp(a).unwrap());
        }
    }

    fn _values(&'a self) -> &'a Vec<f32> {
        &self._list
    }

    fn max(&'a self) -> f32 {
        self._values()
            .iter()
            .fold(f32::NEG_INFINITY, |x, &y| x.max(y))
    }

    fn min(&'a self) -> f32 {
        self._values().iter().fold(f32::INFINITY, |x, &y| x.min(y))
    }
}

#[pyproto]
impl PySequenceProtocol for FloatList {
    fn __len__(&self) -> usize {
        self.size()
    }
}

/// List for i32.
#[pyclass]
struct IntegerList {
    _list: Vec<i32>,
}

#[pymethods]
impl IntegerList {
    #[new]
    fn new(list: Vec<i32>) -> Self {
        List::_new(list)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        List::filter(self, condition)
    }

    pub fn max(&self) -> i32 {
        List::max(self)
    }

    pub fn mean(&self) -> f32 {
        List::mean(self)
    }

    pub fn min(&self) -> i32 {
        List::min(self)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) -> Self {
        List::sort(self, ascending)
    }

    pub fn sum(&self) -> i32 {
        List::sum(self)
    }

    pub fn to_list(&self) -> Vec<i32> {
        List::to_list(self)
    }

    pub fn unique(&self) -> Self {
        List::unique(self)
    }
}

impl<'a> List<'a, i32> for IntegerList {
    fn _new(list: Vec<i32>) -> Self {
        Self { _list: list }
    }

    fn _sort(&self, list: &mut Vec<i32>, ascending: bool) {
        if ascending {
            list.sort();
        } else {
            list.sort_by(|a, b| b.cmp(a))
        }
    }

    fn _values(&'a self) -> &'a Vec<i32> {
        &self._list
    }

    fn max(&'a self) -> i32 {
        *self._values().iter().max().unwrap()
    }

    fn min(&'a self) -> i32 {
        *self._values().iter().min().unwrap()
    }
}

#[pyproto]
impl PySequenceProtocol for IntegerList {
    fn __len__(&self) -> usize {
        self.size()
    }
}

/// List for bool.
#[pyclass]
struct BooleanList {
    _list: Vec<bool>,
}

#[pymethods]
impl BooleanList {
    #[new]
    fn new(list: Vec<bool>) -> Self {
        BooleanList { _list: list }
    }
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ulist(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<FloatList>()?;
    m.add_class::<IntegerList>()?;
    m.add_class::<BooleanList>()?;

    Ok(())
}
