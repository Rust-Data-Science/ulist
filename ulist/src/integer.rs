use crate::base::List;
use crate::boolean::BooleanList;
use crate::float::FloatList;
use crate::numerical::NumericalList;
use pyo3::exceptions::PyIndexError;
use pyo3::prelude::*;

/// List with integer type elements.
#[pyclass]
pub struct IntegerList {
    _values: Vec<i32>,
}

#[pymethods]
impl IntegerList {
    // Arrange the following methods in alphabetical order.

    #[new]
    fn new(vec: Vec<i32>) -> Self {
        List::_new(vec)
    }

    pub fn add(&self, other: &Self) -> Self {
        NumericalList::add(self, other)
    }

    pub fn add_scala(&self, num: i32) -> Self {
        NumericalList::add_scala(self, num)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn div(&self, other: &Self) -> FloatList {
        let vec = NumericalList::div(self, other);
        List::_new(vec)
    }

    pub fn div_scala(&self, num: f32) -> FloatList {
        let vec = NumericalList::div_scala(self, num);
        List::_new(vec)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        NumericalList::filter(self, condition)
    }

    pub fn get(&self, index: usize) -> PyResult<i32> {
        if index < self.size() {
            Ok(List::get(self, index))
        } else {
            Err(PyIndexError::new_err("Index out of range!"))
        }
    }

    pub fn max(&self) -> i32 {
        NumericalList::max(self)
    }

    pub fn mean(&self) -> f32 {
        NumericalList::mean(self)
    }

    pub fn min(&self) -> i32 {
        NumericalList::min(self)
    }

    pub fn mul(&self, other: &Self) -> Self {
        NumericalList::mul(self, other)
    }

    pub fn mul_scala(&self, num: i32) -> Self {
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

    pub fn sub_scala(&self, num: i32) -> Self {
        NumericalList::sub_scala(self, num)
    }

    pub fn sum(&self) -> i32 {
        NumericalList::sum(self)
    }

    pub fn to_list(&self) -> Vec<i32> {
        List::to_list(self)
    }

    pub fn unique(&self) -> Self {
        NumericalList::unique(self)
    }
}

impl<'a> List<'a, i32> for IntegerList {
    fn _new(vec: Vec<i32>) -> Self {
        Self { _values: vec }
    }

    fn values(&self) -> &Vec<i32> {
        &self._values
    }
}

impl<'a> NumericalList<'a, i32> for IntegerList {
    fn _sort(&self, vec: &mut Vec<i32>, ascending: bool) {
        if ascending {
            vec.sort();
        } else {
            vec.sort_by(|a, b| b.cmp(a))
        }
    }

    fn div(&'a self, other: &'a Self) -> Vec<f32> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(&x, &y)| x as f32 / y as f32)
            .collect()
    }

    fn div_scala(&'a self, num: f32) -> Vec<f32> {
        self.values().iter().map(|x| *x as f32 / num).collect()
    }

    fn max(&'a self) -> i32 {
        *self.values().iter().max().unwrap()
    }

    fn min(&'a self) -> i32 {
        *self.values().iter().min().unwrap()
    }
}
