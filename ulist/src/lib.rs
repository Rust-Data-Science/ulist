mod base;
mod boolean;
mod control_flow;
mod float;
mod index;
mod integers;
mod non_float;
mod numerical;
mod string;
mod types;
use control_flow::*;
use pyo3::prelude::*;

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ulist(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<boolean::BooleanList>()?;
    m.add_class::<float::FloatList>()?;
    m.add_class::<integers::IntegerList32>()?;
    m.add_class::<integers::IntegerList64>()?;
    m.add_class::<string::StringList>()?;
    m.add_class::<index::IndexList>()?;
    m.add_function(wrap_pyfunction!(integers::arange32, m)?)?;
    m.add_function(wrap_pyfunction!(integers::arange64, m)?)?;
    m.add_function(wrap_pyfunction!(select_bool, m)?)?;
    m.add_function(wrap_pyfunction!(select_float, m)?)?;
    m.add_function(wrap_pyfunction!(select_int, m)?)?;
    m.add_function(wrap_pyfunction!(select_string, m)?)?;

    Ok(())
}
