use crate::base::List;
use crate::boolean::BooleanList;
use crate::float::FloatList;
use crate::integer::IntegerList;
use pyo3::prelude::*;
use pyo3::Py;
use std::cmp::PartialEq;
use std::marker::Copy;

unsafe fn select<T, U>(
    py: Python,
    conditions: &Vec<Py<BooleanList>>,
    choices: &Vec<T>,
    default: T,
) -> U
where
    T: PartialEq + Copy,
    U: List<T>,
{
    let cond: Vec<PyRef<BooleanList>> = conditions.iter().map(|x| x.borrow(py)).collect();
    let mut vec = vec![default; cond[0].size()];
    for j in 0..cond[0].size() {
        for i in 0..cond.len() {
            if cond[i].get(j) {
                vec[j] = choices[i];
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
    choices: Vec<i32>,
    default: i32,
) -> IntegerList {
    select::<i32, IntegerList>(py, &conditions, &choices, default)
}
