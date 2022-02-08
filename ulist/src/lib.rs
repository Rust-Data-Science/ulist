mod base;
mod boolean;
mod control_flow;
mod float;
mod integer;
mod non_float;
mod numerical;
mod string;
mod types;
use control_flow::*;
use pyo3::prelude::*;

// Cannot find a way to put this function in another file.
#[pyfunction]
pub fn arange(start: i32, stop: i32, step: usize) -> integer::IntegerList {
    let vec = (start..stop).step_by(step).collect();
    integer::IntegerList::new(vec)
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ulist(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<boolean::BooleanList>()?;
    m.add_class::<float::FloatList>()?;
    m.add_class::<integer::IntegerList>()?;
    m.add_class::<string::StringList>()?;
    m.add_function(wrap_pyfunction!(arange, m)?)?;
    m.add_function(wrap_pyfunction!(select_bool, m)?)?;
    m.add_function(wrap_pyfunction!(select_float, m)?)?;
    m.add_function(wrap_pyfunction!(select_int, m)?)?;
    m.add_function(wrap_pyfunction!(select_str, m)?)?;

    Ok(())
}
