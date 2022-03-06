use crate::base::List;
use crate::float::FloatList;
use crate::index::IndexList;
use crate::integer::IntegerList;
use crate::non_float::NonFloatList;
use crate::string::StringList;
use crate::types::AsFloatList;
use crate::types::AsIntegerList;
use crate::types::AsStringList;
use pyo3::prelude::*;
use std::cell::Ref;
use std::cell::RefCell;
use std::cell::RefMut;
use std::collections::HashMap;
use std::ops::Fn;

/// List with boolean type elements.
#[pyclass]
pub struct BooleanList {
    _values: RefCell<Vec<bool>>,
}

#[pymethods]
impl BooleanList {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<bool>) -> Self {
        List::_new(vec)
    }

    pub fn all(&self) -> bool {
        self.values().iter().all(|&x| x)
    }

    pub fn and_(&self, other: &Self) -> Self {
        _logical_operate(&self, &other, |x, y| x && y)
    }

    pub fn any(&self) -> bool {
        self.values().iter().any(|&x| x)
    }

    pub fn append(&self, elem: bool) {
        List::append(self, elem)
    }

    pub fn as_float(&self) -> FloatList {
        AsFloatList::as_float(self)
    }

    pub fn as_int(&self) -> IntegerList {
        AsIntegerList::as_int(self)
    }

    pub fn as_str(&self) -> StringList {
        AsStringList::as_str(self)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn counter(&self) -> HashMap<bool, usize> {
        NonFloatList::counter(self)
    }

    #[staticmethod]
    pub fn cycle(vec: Vec<bool>, size: usize) -> Self {
        List::cycle(&vec, size)
    }

    pub fn equal_scala(&self, elem: bool) -> BooleanList {
        List::equal_scala(self, elem)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        List::filter(self, condition)
    }

    pub unsafe fn get(&self, index: usize) -> bool {
        List::get(self, index)
    }

    pub fn not_(&self) -> Self {
        let vec = self.values().iter().map(|&x| !x).collect();
        BooleanList::new(vec)
    }

    pub fn not_equal_scala(&self, elem: bool) -> BooleanList {
        List::not_equal_scala(self, elem)
    }

    pub fn or_(&self, other: &Self) -> Self {
        _logical_operate(&self, &other, |x, y| x || y)
    }

    pub fn pop(&self) {
        List::pop(self);
    }

    #[staticmethod]
    pub fn repeat(elem: bool, size: usize) -> Self {
        List::repeat(elem, size)
    }

    pub fn replace(&self, old: bool, new: bool) -> Self {
        List::replace(self, old, new)
    }

    pub unsafe fn set(&self, index: usize, elem: bool) {
        List::set(self, index, elem)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) -> Self {
        NonFloatList::sort(self, ascending)
    }

    pub fn sum(&self) -> i32 {
        self.values().iter().map(|&x| if x { 1 } else { 0 }).sum()
    }

    pub fn to_index(&self) -> IndexList {
        let vec = self
            .values()
            .iter()
            .enumerate()
            .filter(|(_, y)| **y)
            .map(|(x, _)| x.clone())
            .collect();
        IndexList::new(vec)
    }

    pub fn to_list(&self) -> Vec<bool> {
        List::to_list(self)
    }

    pub fn union_all(&self, other: &Self) -> Self {
        List::union_all(self, other)
    }

    pub fn unique(&self) -> Self {
        NonFloatList::unique(self)
    }
}

impl List<bool> for BooleanList {
    fn _new(vec: Vec<bool>) -> Self {
        Self {
            _values: RefCell::new(vec),
        }
    }

    fn values(&self) -> Ref<Vec<bool>> {
        self._values.borrow()
    }

    fn values_mut(&self) -> RefMut<Vec<bool>> {
        self._values.borrow_mut()
    }
}

impl NonFloatList<bool> for BooleanList {}

fn _logical_operate(
    this: &BooleanList,
    other: &BooleanList,
    func: impl Fn(bool, bool) -> bool,
) -> BooleanList {
    let vec = this
        .values()
        .iter()
        .zip(other.values().iter())
        .map(|(&x, &y)| func(x, y))
        .collect();
    BooleanList::new(vec)
}

impl AsFloatList for BooleanList {
    fn as_float(&self) -> FloatList {
        let vec = self
            .values()
            .iter()
            .map(|&x| if x { 1.0 } else { 0.0 })
            .collect();
        FloatList::new(vec)
    }
}

impl AsIntegerList for BooleanList {
    fn as_int(&self) -> IntegerList {
        let vec = self
            .values()
            .iter()
            .map(|&x| if x { 1 } else { 0 })
            .collect();
        IntegerList::new(vec)
    }
}

impl AsStringList for BooleanList {
    fn as_str(&self) -> StringList {
        let vec = self.values().iter().map(|&x| x.to_string()).collect();
        StringList::new(vec)
    }
}
