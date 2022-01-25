use crate::base::List;
use pyo3::prelude::*;
use std::cell::Ref;
use std::cell::RefCell;
use std::cell::RefMut;
use std::collections::HashMap;

/// List with string type elements.
#[pyclass]
pub struct StringList {
    _values: RefCell<Vec<String>>,
}

#[pymethods]
impl StringList {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<String>) -> Self {
        List::_new(vec)
    }

    pub fn append(&self, elem: String) {
        List::append(self, elem)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    // TODO: Inherit this from `List` trait.
    pub fn counter(&self) -> HashMap<String, usize> {
        let mut _result: HashMap<&str, usize> = HashMap::new();
        let vec = self.values();
        for key in vec.iter() {
            let val = _result.entry(key).or_insert(0);
            *val += 1;
        }

        let mut result: HashMap<String, usize> = HashMap::with_capacity(_result.capacity());
        for (&key, &val) in _result.iter() {
            result.insert(key.to_string(), val);
        }
        result
    }

    #[staticmethod]
    pub fn cycle(vec: Vec<String>, size: usize) -> Self {
        List::cycle(&vec, size)
    }

    pub unsafe fn get(&self, index: usize) -> String {
        List::get(self, index)
    }

    pub fn pop(&self) {
        List::pop(self);
    }

    #[staticmethod]
    pub fn repeat(elem: String, size: usize) -> Self {
        List::repeat(elem, size)
    }

    pub unsafe fn set(&self, index: usize, elem: String) {
        List::set(self, index, elem)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn to_list(&self) -> Vec<String> {
        List::to_list(self)
    }

    pub fn union_all(&self, other: &Self) -> Self {
        List::union_all(self, other)
    }
}

impl List<String> for StringList {
    fn _new(vec: Vec<String>) -> Self {
        Self {
            _values: RefCell::new(vec),
        }
    }

    fn values(&self) -> Ref<Vec<String>> {
        self._values.borrow()
    }

    fn values_mut(&self) -> RefMut<Vec<String>> {
        self._values.borrow_mut()
    }
}
