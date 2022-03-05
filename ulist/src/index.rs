use pyo3::prelude::*;

#[pyclass]
pub struct IndexList {
    _values: Vec<u32>,
}

#[pymethods]
impl IndexList {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<u32>) -> Self {
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

    pub fn back(&self) -> u32 {
        self._values[self._values.len() - 1]
    }

    pub fn to_list(&self) -> Vec<u32> {
        self._values.clone()
    }
}
