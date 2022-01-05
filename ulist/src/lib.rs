mod base;
mod boolean;
mod float;
mod integer;
mod numerical;
mod types;
use integer::IntegerList;
use pyo3::prelude::*;

// Cannot find a way to put this function in another file.
#[pyfunction]
pub fn arange(start: i32, stop: i32, step: usize) -> IntegerList {
    let vec = (start..stop).step_by(step).collect();
    IntegerList::new(vec)
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ulist(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<boolean::BooleanList>()?;
    m.add_class::<float::FloatList>()?;
    m.add_class::<integer::IntegerList>()?;
    m.add_function(wrap_pyfunction!(arange, m)?)?;

    Ok(())
}
