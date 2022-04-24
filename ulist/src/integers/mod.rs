mod int32;
mod int64;
pub use int32::IntegerList32;
pub use int64::IntegerList64;
use pyo3::prelude::*;
use std::collections::HashSet;

#[pyfunction]
pub fn arange32(start: i32, stop: i32, step: usize) -> IntegerList32 {
    let vec = (start..stop).step_by(step).collect();
    IntegerList32::new(vec, HashSet::new())
}

#[pyfunction]
pub fn arange64(start: i64, stop: i64, step: usize) -> IntegerList64 {
    let vec = (start..stop).step_by(step).collect();
    IntegerList64::new(vec, HashSet::new())
}
