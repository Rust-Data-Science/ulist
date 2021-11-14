use num::traits::AsPrimitive;
use pyo3::class::sequence::PySequenceProtocol;
use pyo3::prelude::*;
use std::iter::Sum;

/// An abstract List.
trait List<'a, T>
where
    T: AsPrimitive<f32> + Sum<&'a T>,
{
    fn values(&'a self) -> &'a Vec<T>;

    // Arrange the following methods in alphabetical order.
    fn max(&'a self) -> T;

    fn mean(&'a self) -> f32 {
        let numeritor: f32 = self.sum().as_();
        let denominator: f32 = self.size().as_();
        numeritor / denominator
    }

    fn min(&'a self) -> T;

    fn size(&'a self) -> usize {
        self.values().len()
    }

    fn sum(&'a self) -> T {
        self.values().iter().sum()
    }
}

/// List for f32.
#[pyclass]
struct FloatList {
    list: Vec<f32>,
}

#[pymethods]
impl FloatList {
    #[new]
    fn new(list: Vec<f32>) -> Self {
        FloatList { list }
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

    pub fn sum(&self) -> f32 {
        List::sum(self)
    }
}

impl<'a> List<'a, f32> for FloatList {
    fn values(&'a self) -> &'a Vec<f32> {
        &self.list
    }

    fn max(&'a self) -> f32 {
        self.values()
            .iter()
            .fold(f32::NEG_INFINITY, |x, &y| x.max(y))
    }

    fn min(&'a self) -> f32 {
        self.values().iter().fold(f32::INFINITY, |x, &y| x.min(y))
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
    list: Vec<i32>,
}

#[pymethods]
impl IntegerList {
    #[new]
    fn new(list: Vec<i32>) -> Self {
        IntegerList { list }
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

    pub fn sum(&self) -> i32 {
        List::sum(self)
    }
}

impl<'a> List<'a, i32> for IntegerList {
    fn values(&'a self) -> &'a Vec<i32> {
        &self.list
    }

    fn max(&'a self) -> i32 {
        *self.values().iter().max().unwrap()
    }

    fn min(&'a self) -> i32 {
        *self.values().iter().min().unwrap()
    }
}

#[pyproto]
impl PySequenceProtocol for IntegerList {
    fn __len__(&self) -> usize {
        self.size()
    }
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ulist(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<FloatList>()?;
    m.add_class::<IntegerList>()?;

    Ok(())
}
