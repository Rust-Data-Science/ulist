use crate::base::List;
use pyo3::exceptions::PyIndexError;
use pyo3::prelude::*;
use std::ops::Fn;

/// List with boolean type elements.
#[pyclass]
pub struct BooleanList {
    _values: Vec<bool>,
}

#[pymethods]
impl BooleanList {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<bool>) -> Self {
        BooleanList { _values: vec }
    }

    pub fn all(&self) -> bool {
        self.values().iter().all(|&x| x)
    }

    pub fn and_(&self, other: &Self) -> Self {
        _logical_operate(&self, &other, |x, y| x && y)
    }

    pub fn any(&self) -> bool {
        self.values().iter().any(|&x| x)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn get(&self, index: usize) -> PyResult<bool> {
        if index < self.size() {
            Ok(List::get(self, index))
        } else {
            Err(PyIndexError::new_err("Index out of range!"))
        }
    }

    pub fn not_(&self) -> Self {
        let vec = self.values().iter().map(|&x| !x).collect();
        BooleanList::new(vec)
    }

    pub fn or_(&self, other: &Self) -> Self {
        _logical_operate(&self, &other, |x, y| x || y)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn to_list(&self) -> Vec<bool> {
        List::to_list(self)
    }
}

impl<'a> List<'a, bool> for BooleanList {
    fn _new(vec: Vec<bool>) -> Self {
        Self { _values: vec }
    }

    fn values(&self) -> &Vec<bool> {
        &self._values
    }
}

fn _logical_operate(
    this: &BooleanList,
    other: &BooleanList,
    func: impl Fn(bool, bool) -> bool,
) -> BooleanList {
    let vec = this
        .values()
        .iter()
        .zip(other.values().iter())
        .map(|(&x, &y)| func(x, y))
        .collect();
    BooleanList::new(vec)
}
