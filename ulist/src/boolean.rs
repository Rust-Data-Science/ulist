use crate::base::List;
use pyo3::exceptions::PyIndexError;
use pyo3::prelude::*;

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
