use pyo3::prelude::*;

#[pyclass]
pub struct IndexList {
    _values: Vec<u32>,
}

#[pymethods]
impl IndexList {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<u32>) -> Self {
        IndexList { _values: vec }
    }

    pub fn back(&self) -> u32 {
        self._values[self._values.len()]
    }
}
