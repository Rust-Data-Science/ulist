use pyo3::prelude::*;

#[pyclass]
pub struct IndexList {
    _values: Vec<u32>,
}
