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

    pub fn sum(&self) -> i32 {
        self.values.iter().sum()
    }

    pub fn min(&self) -> i32 {
        *self.values.iter().min().unwrap()
    }

    pub fn max(&self) -> i32 {
        *self.values.iter().max().unwrap()
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
