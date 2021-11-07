use pyo3::class::sequence::PySequenceProtocol;
use pyo3::prelude::*;

/// A class to bind Rust Vector.
#[pyclass]
struct List {
    values: Vec<i32>,
    dtype: String,
}

#[pymethods]
impl List {
    #[new]
    fn new(values: Vec<i32>, dtype: String) -> Self {
        List { values, dtype }
    }

    // Arrange the following methods in alphabetical order.
    pub fn max(&self) -> i32 {
        *self.values.iter().max().unwrap()
    }
    pub fn mean(&self) -> f32 {
        self.sum() as f32 / self.values.len() as f32
    }

    pub fn min(&self) -> i32 {
        *self.values.iter().min().unwrap()
    }

    pub fn size(&self) -> usize {
        self.values.len()
    }

    pub fn sum(&self) -> i32 {
        self.values.iter().sum()
    }
}

#[pyproto]
impl PySequenceProtocol for List {
    fn __len__(&self) -> usize {
        self.values.len()
    }
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ulist(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<List>()?;

    Ok(())
}
