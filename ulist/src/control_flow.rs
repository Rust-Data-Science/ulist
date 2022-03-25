use crate::base::List;
use crate::boolean::BooleanList;
use crate::float::FloatList;
use crate::integers::IntegerList64;
use crate::string::StringList;
use pyo3::prelude::*;
use pyo3::Py;

unsafe fn select<T, U>(
    py: Python,
    conditions: &Vec<Py<BooleanList>>,
    choices: &Vec<T>,
    default: T,
) -> U
where
    T: PartialEq + Clone,
    U: List<T>,
{
    let cond: Vec<PyRef<BooleanList>> = conditions.iter().map(|x| x.borrow(py)).collect();
    let mut vec = vec![default; cond[0].size()];
    for j in 0..cond[0].size() {
        for i in 0..cond.len() {
            if cond[i].get(j) {
                vec[j] = choices[i].clone();
                break;
            }
        }
    }
    U::_new(vec)
}

#[pyfunction]
pub unsafe fn select_bool(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<bool>,
    default: bool,
) -> BooleanList {
    select::<bool, BooleanList>(py, &conditions, &choices, default)
}

#[pyfunction]
pub unsafe fn select_float(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<f32>,
    default: f32,
) -> FloatList {
    select::<f32, FloatList>(py, &conditions, &choices, default)
}

#[pyfunction]
pub unsafe fn select_int(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<i64>,
    default: i64,
) -> IntegerList64 {
    select::<i64, IntegerList64>(py, &conditions, &choices, default)
}

#[pyfunction]
pub unsafe fn select_string(
    py: Python,
    conditions: Vec<Py<BooleanList>>,
    choices: Vec<String>,
    default: String,
) -> StringList {
    select::<String, StringList>(py, &conditions, &choices, default)
}
