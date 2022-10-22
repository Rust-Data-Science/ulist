use pyo3::prelude::*;

#[pyclass]
pub struct IndexList {
    _values: Vec<usize>,
}

impl IndexList {
    pub fn values(&self) -> &Vec<usize> {
        &self._values
    }
}

#[pymethods]
impl IndexList {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<usize>) -> Self {
        IndexList { _values: vec }
    }

    fn __repr__(&self) -> String {
        format!("IndexList({})", self.__str__())
    }

    fn __str__(&self) -> String {
        let v = &self._values;
        let n = v.len();
        if n < 100 {
            format!("{:?}", self._values)
        } else {
            format!(
                "[{}, {}, {}, ..., {}, {}, {}]",
                v[0],
                v[1],
                v[2],
                v[n - 3],
                v[n - 2],
                v[n - 1]
            )
        }
    }

    pub fn back(&self) -> usize {
        self._values[self._values.len() - 1]
    }

    pub fn to_list(&self) -> Vec<usize> {
        self._values.clone()
    }

    pub fn size(&self) -> usize {
        self._values.len()
    }
}
