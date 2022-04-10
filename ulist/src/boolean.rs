use crate::base::List;
use crate::floatings::FloatList32;
use crate::floatings::FloatList64;
use crate::index::IndexList;
use crate::integers::IntegerList32;
use crate::integers::IntegerList64;
use crate::non_float::NonFloatList;
use crate::string::StringList;
use crate::types::AsFloatList32;
use crate::types::AsFloatList64;
use crate::types::AsIntegerList32;
use crate::types::AsIntegerList64;
use crate::types::AsStringList;
use pyo3::prelude::*;
use std::cell::Ref;
use std::cell::RefCell;
use std::cell::RefMut;
use std::collections::HashMap;
use std::collections::HashSet;
use std::ops::Fn;

/// List with boolean type elements.
#[pyclass]
pub struct BooleanList {
    _values: RefCell<Vec<bool>>,
    _missing_values: RefCell<HashSet<usize>>,
}

#[pymethods]
impl BooleanList {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<bool>, hset: HashSet<usize>) -> Self {
        List::_new(vec, hset)
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

    pub fn as_float32(&self) -> FloatList32 {
        AsFloatList32::as_float32(self)
    }

    pub fn as_float64(&self) -> FloatList64 {
        AsFloatList64::as_float64(self)
    }

    pub fn as_int32(&self) -> IntegerList32 {
        AsIntegerList32::as_int32(self)
    }

    pub fn as_int64(&self) -> IntegerList64 {
        AsIntegerList64::as_int64(self)
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

    pub fn get(&self, index: usize) -> bool {
        List::get(self, index)
    }

    pub unsafe fn get_by_indexes(&self, indexes: &IndexList) -> Self {
        List::get_by_indexes(self, indexes)
    }

    pub fn not_(&self) -> Self {
        let vec = self.values().iter().map(|&x| !x).collect();
        BooleanList::new(vec, HashSet::new())
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
    fn _new(vec: Vec<bool>, hset: HashSet<usize>) -> Self {
        Self {
            _values: RefCell::new(vec),
            _missing_values: RefCell::new(hset),
        }
    }

    fn missing_values(&self) -> Ref<HashSet<usize>> {
        self._missing_values.borrow()
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
    BooleanList::new(vec, HashSet::new())
}

impl AsFloatList32 for BooleanList {
    fn as_float32(&self) -> FloatList32 {
        let vec = self
            .values()
            .iter()
            .map(|&x| if x { 1.0 } else { 0.0 })
            .collect();
        FloatList32::new(vec)
    }
}

impl AsFloatList64 for BooleanList {
    fn as_float64(&self) -> FloatList64 {
        let vec = self
            .values()
            .iter()
            .map(|&x| if x { 1.0 } else { 0.0 })
            .collect();
        FloatList64::new(vec)
    }
}

impl AsIntegerList32 for BooleanList {
    fn as_int32(&self) -> IntegerList32 {
        let vec = self
            .values()
            .iter()
            .map(|&x| if x { 1 } else { 0 })
            .collect();
        IntegerList32::new(vec)
    }
}

impl AsIntegerList64 for BooleanList {
    fn as_int64(&self) -> IntegerList64 {
        let vec = self
            .values()
            .iter()
            .map(|&x| if x { 1 } else { 0 })
            .collect();
        IntegerList64::new(vec)
    }
}

impl AsStringList for BooleanList {
    fn as_str(&self) -> StringList {
        let vec = self.values().iter().map(|&x| x.to_string()).collect();
        StringList::new(vec)
    }
}
