use crate::base::List;
use crate::boolean::BooleanList;
use crate::floatings::FloatList64;
use crate::integers::IntegerList64;
use crate::string::StringList;
use pyo3::exceptions::PyRuntimeError;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::Py;
use std::collections::HashSet;

fn select<T, U>(
    py: Python,
    conditions: &[Py<BooleanList>],
    choices: &[T],
    default: T,
) -> PyResult<U>
where
    T: PartialEq + Clone,
    U: List<T>,
{
    let cond: Vec<PyRef<BooleanList>> = conditions.iter().map(|x| x.borrow(py)).collect();
    let n = cond[0].size();
    for c in cond.iter() {
        if c.size() != n {
            return Err(PyRuntimeError::new_err(
                "BooleanList sizes in conditions should be equal!",
            ));
        } else if c.count_na() > 0 {
            return Err(PyValueError::new_err(
                "Parameter `condition` should not contain missing values!",
            ));
        }
    }

    let mut vec = vec![default; cond[0].size()];
    for j in 0..vec.len() {
        for i in 0..cond.len() {
            let ptr = unsafe { cond.get_unchecked(i) };
            let choice = unsafe { choices.get_unchecked(i) };
            // TODO: implement iter() for BooleanList
            if ptr.get(j).unwrap().unwrap() {
                vec[j] = choice.clone();
                break;
            }
        }
    }
    Ok(U::_new(vec, HashSet::new()))
}

#[pyfunction]
pub fn select_bool(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<bool>,
    default: bool,
) -> PyResult<BooleanList> {
    select::<bool, BooleanList>(py, &conditions, &choices, default)
}

#[pyfunction]
pub fn select_float(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<f64>,
    default: f64,
) -> PyResult<FloatList64> {
    select::<f64, FloatList64>(py, &conditions, &choices, default)
}

#[pyfunction]
pub fn select_int(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<i64>,
    default: i64,
) -> PyResult<IntegerList64> {
    select::<i64, IntegerList64>(py, &conditions, &choices, default)
}

#[pyfunction]
pub fn select_string(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<String>,
    default: String,
) -> PyResult<StringList> {
    select::<String, StringList>(py, &conditions, &choices, default)
}
