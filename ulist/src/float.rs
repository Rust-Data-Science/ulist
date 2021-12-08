use crate::base::List;
use crate::boolean::BooleanList;
use crate::numerical::NumericalList;
use pyo3::exceptions::PyIndexError;
use pyo3::prelude::*;

/// List with float type elements.
#[pyclass]
pub struct FloatList {
    _values: Vec<f32>,
}

#[pymethods]
impl FloatList {
    // Arrange the following methods in alphabetical order.

    #[new]
    fn new(vec: Vec<f32>) -> Self {
        List::_new(vec)
    }

    pub fn add(&self, other: &Self) -> Self {
        NumericalList::add(self, other)
    }

    pub fn add_scala(&self, num: f32) -> Self {
        NumericalList::add_scala(self, num)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn div(&self, other: &Self) -> Self {
        let vec = NumericalList::div(self, other);
        List::_new(vec)
    }

    pub fn div_scala(&self, num: f32) -> Self {
        let vec = NumericalList::div_scala(self, num);
        List::_new(vec)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        NumericalList::filter(self, condition)
    }

    pub fn get(&self, index: usize) -> PyResult<f32> {
        if index < self.size() {
            Ok(List::get(self, index))
        } else {
            Err(PyIndexError::new_err("Index out of range!"))
        }
    }

    pub fn max(&self) -> f32 {
        NumericalList::max(self)
    }

    pub fn mean(&self) -> f32 {
        NumericalList::mean(self)
    }

    pub fn min(&self) -> f32 {
        NumericalList::min(self)
    }

    pub fn mul(&self, other: &Self) -> Self {
        NumericalList::mul(self, other)
    }

    pub fn mul_scala(&self, num: f32) -> Self {
        NumericalList::mul_scala(self, num)
    }

    pub fn pow_scala(&self, num: usize) -> Self {
        NumericalList::pow_scala(self, num)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) -> Self {
        NumericalList::sort(self, ascending)
    }

    pub fn sub(&self, other: &Self) -> Self {
        NumericalList::sub(self, other)
    }

    pub fn sub_scala(&self, num: f32) -> Self {
        NumericalList::sub_scala(self, num)
    }

    pub fn sum(&self) -> f32 {
        NumericalList::sum(self)
    }

    pub fn to_list(&self) -> Vec<f32> {
        List::to_list(self)
    }

    pub fn unique(&self) -> Self {
        NumericalList::unique(self)
    }
}

impl<'a> List<'a, f32> for FloatList {
    fn _new(vec: Vec<f32>) -> Self {
        Self { _values: vec }
    }

    fn values(&self) -> &Vec<f32> {
        &self._values
    }
}

impl<'a> NumericalList<'a, f32> for FloatList {
    fn _sort(&self, vec: &mut Vec<f32>, ascending: bool) {
        if ascending {
            vec.sort_by(|a, b| a.partial_cmp(b).unwrap());
        } else {
            vec.sort_by(|a, b| b.partial_cmp(a).unwrap());
        }
    }

    fn div(&'a self, other: &Self) -> Vec<f32> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(x, y)| x / y)
            .collect()
    }

    fn div_scala(&'a self, num: f32) -> Vec<f32> {
        self.values().iter().map(|x| *x / num).collect()
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
