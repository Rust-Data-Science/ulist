use crate::boolean::BooleanList;
use crate::floatings::FloatList64;
use crate::integers::IntegerList64;
use crate::string::StringList;
use pyo3::prelude::*;
use std::collections::HashSet;
use std::iter::FromIterator;

#[pyfunction]
pub fn read_csv(py: Python) -> Vec<PyObject> {
    // This is an example implementation of `read_csv` function, which will return
    // PyList[BooleanList[True, False, None], IntegerList64[2, 3, None],
    // FloatList64[2.0, 3.0, None], StringList['foo', 'bar', None]]
    let blist = BooleanList::new(vec![true, false, false], HashSet::from_iter(vec![2]));
    let ilist = IntegerList64::new(vec![2, 3, 0], HashSet::from_iter(vec![2]));
    let flist = FloatList64::new(vec![2.0, 3.0, 0.0], HashSet::from_iter(vec![2]));
    let slist = StringList::new(
        vec!["foo".to_string(), "bar".to_string(), "".to_string()],
        HashSet::from_iter(vec![2]),
    );
    let mut result: Vec<PyObject> = Vec::new();
    result.push(blist.into_py(py));
    result.push(ilist.into_py(py));
    result.push(flist.into_py(py));
    result.push(slist.into_py(py));
    return result;
}
