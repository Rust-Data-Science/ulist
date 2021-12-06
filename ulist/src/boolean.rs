use crate::base::List;
use pyo3::prelude::*;

/// List with boolean type elements.
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

impl<'a> List<'a, bool> for BooleanList {
    fn _new(vec: Vec<bool>) -> Self {
        Self { _values: vec }
    }

    fn values(&self) -> &Vec<bool> {
        &self._values
    }
}
