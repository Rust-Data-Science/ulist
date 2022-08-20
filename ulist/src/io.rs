use crate::boolean::BooleanList;
use crate::floatings::{FloatList32, FloatList64};
use crate::integers::{IntegerList32, IntegerList64};
use crate::string::StringList;
use pyo3::exceptions::{PyIOError, PyTypeError, PyValueError};
use pyo3::prelude::*;
use std::collections::{HashMap, HashSet};
use std::str::FromStr;

/// Read `csv` from path. May fail.
/// `schema` is a vector contains the `(field, type)` tuples.
#[pyfunction]
pub fn read_csv(
    path: String,
    schema: Vec<(String, String)>,
    py: Python,
) -> PyResult<Vec<PyObject>> {
    let mut reader = match csv::Reader::from_path(path) {
        Err(e) => return Err(PyIOError::new_err(e.to_string())),
        Ok(reader) => reader,
    };

    // Get records from reader.
    let mut records: HashMap<&String, Vec<String>> = HashMap::new();
    let headers: Vec<String> = match reader.headers() {
        Ok(headers) => headers.into_iter().map(|s| s.trim().into()).collect(),
        Err(e) => return Err(PyIOError::new_err(e.to_string())),
    };
    for record in reader.records() {
        match record {
            Err(e) => return Err(PyIOError::new_err(e.to_string())),
            Ok(record) => {
                for (idx, entry) in record.into_iter().enumerate() {
                    let entry = &entry.trim().replace("\r\n", "\n");
                    records
                        .entry(&headers[idx])
                        .and_modify(|v| v.push(entry.into()))
                        .or_insert_with(|| vec![entry.into()]);
                }
            }
        }
    }

    // Cast `records` to `PyObject`.
    let mut result = Vec::new();
    for (header, t) in schema.iter() {
        if let Some(list) = records.remove(header) {
            result.push(get_pylist(t, list, py)?);
        } else {
            result.push(get_pylist(t, Vec::new(), py)?);
        }
    }
    Ok(result)
}

/// Get a translated `python list` from a `rust list` with the given type `t`.
fn get_pylist(t: &str, list: Vec<String>, py: Python) -> PyResult<PyObject> {
    let res = match t {
        // TODO: <24-05-22, yingmanwumen> Write a macro to uncurry, for example:
        // ```
        // IntegerList64::new(uncurry!(parse_vstr(list)?)).into_py(py)
        // ```
        "int" | "int64" => {
            let (vec, hset) = parse_vec(list, |e| e.parse())?;
            IntegerList64::new(vec, hset).into_py(py)
        }
        "int32" => {
            let (vec, hset) = parse_vec(list, |e| e.parse())?;
            IntegerList32::new(vec, hset).into_py(py)
        }
        "float" | "float64" => {
            let (vec, hset) = parse_vec(list, |e| e.parse())?;
            FloatList64::new(vec, hset).into_py(py)
        }
        "float32" => {
            let (vec, hset) = parse_vec(list, |e| e.parse())?;
            FloatList32::new(vec, hset).into_py(py)
        }
        "bool" => {
            // `to_ascii_lowercase` maps `True` to `true`
            let (vec, hset) = parse_vec(list, |e| e.to_ascii_lowercase().parse())?;
            BooleanList::new(vec, hset).into_py(py)
        }
        "string" => {
            let (vec, hset) = parse_vec(list, |e| e.parse())?;
            StringList::new(vec, hset).into_py(py)
        }
        _ => {
            // Copied from `python/constructor.py`
            return Err(PyValueError::new_err(
                "Parameter dtype should be 'int', 'int32', 'int64', \
                'float', 'float32', 'float64', 'bool' or 'string'!",
            ));
        }
    };
    Ok(res)
}

/// Parse a `Vec<String>` to a `Vec<T>`.
fn parse_vec<T>(
    from: Vec<String>,
    parse: fn(String) -> Result<T, T::Err>,
) -> PyResult<(Vec<T>, HashSet<usize>)>
where
    T: FromStr + Default,
    <T as FromStr>::Err: ToString,
{
    let (mut vec, mut hset) = (Vec::new(), HashSet::new());
    for (idx, item) in from.into_iter().enumerate() {
        if item.is_empty() {
            hset.insert(idx);
            vec.push(T::default());
            continue;
        }
        match parse(item) {
            Ok(s) => vec.push(s),
            Err(e) => return Err(PyTypeError::new_err(e.to_string())),
        }
    }
    Ok((vec, hset))
}
