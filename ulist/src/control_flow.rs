use crate::base::List;
use crate::boolean::BooleanList;
use crate::floatings::FloatList64;
use crate::integers::IntegerList64;
use crate::string::StringList;
use pyo3::prelude::*;
use pyo3::Py;
use std::collections::HashSet;

fn select<T, U>(py: Python, conditions: &Vec<Py<BooleanList>>, choices: &Vec<T>, default: T) -> U
where
    T: PartialEq + Clone,
    U: List<T>,
{
    let cond: Vec<PyRef<BooleanList>> = conditions.iter().map(|x| x.borrow(py)).collect();
    let mut vec = vec![default; cond[0].size()];
    for j in 0..cond[0].size() {
        for i in 0..cond.len() {
            // TODO: Improve the benchmark.
            if cond[i].get(j).unwrap() {
                vec[j] = choices[i].clone();
                break;
            }
        }
    }
    U::_new(vec, HashSet::new())
}

#[pyfunction]
pub fn select_bool(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<bool>,
    default: bool,
) -> BooleanList {
    select::<bool, BooleanList>(py, &conditions, &choices, default)
}

#[pyfunction]
pub fn select_float(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<f64>,
    default: f64,
) -> FloatList64 {
    select::<f64, FloatList64>(py, &conditions, &choices, default)
}

#[pyfunction]
pub fn select_int(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<i64>,
    default: i64,
) -> IntegerList64 {
    select::<i64, IntegerList64>(py, &conditions, &choices, default)
}

#[pyfunction]
pub fn select_string(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<String>,
    default: String,
) -> StringList {
    select::<String, StringList>(py, &conditions, &choices, default)
}
