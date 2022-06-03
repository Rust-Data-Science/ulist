use crate::base::List;
use crate::boolean::BooleanList;
use crate::floatings::FloatList32;
use crate::index::IndexList;
use crate::integers::IntegerList32;
use crate::integers::IntegerList64;
use crate::numerical::NumericalList;
use crate::string::StringList;
use crate::types::AsBooleanList;
use crate::types::AsFloatList32;
use crate::types::AsIntegerList32;
use crate::types::AsIntegerList64;
use crate::types::AsStringList;
use pyo3::prelude::*;
use std::cell::Ref;
use std::cell::RefCell;
use std::cell::RefMut;
use std::collections::HashSet;

/// List with float type elements.
#[pyclass]
pub struct FloatList64 {
    _values: RefCell<Vec<f64>>,
    _na_indexes: RefCell<HashSet<usize>>,
}

#[pymethods]
impl FloatList64 {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<f64>, hset: HashSet<usize>) -> Self {
        List::_new(vec, hset)
    }

    pub fn add(&self, other: &Self) -> PyResult<Self> {
        NumericalList::add(self, other)
    }

    pub fn add_scala(&self, elem: f64) -> Self {
        NumericalList::add_scala(self, elem)
    }

    pub fn all_equal(&self, other: &Self) -> Option<bool> {
        List::all_equal(self, other)
    }

    pub fn append(&self, elem: Option<f64>) {
        List::append(self, elem)
    }

    pub fn argmax(&self) -> PyResult<usize> {
        NumericalList::argmax(self)
    }

    pub fn argmin(&self) -> PyResult<usize> {
        NumericalList::argmin(self)
    }

    pub fn as_bool(&self) -> BooleanList {
        AsBooleanList::as_bool(self)
    }

    pub fn as_float32(&self) -> FloatList32 {
        AsFloatList32::as_float32(self)
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

    pub fn count_na(&self) -> usize {
        List::count_na(self)
    }

    #[staticmethod]
    pub fn cycle(vec: Vec<f64>, size: usize) -> Self {
        List::cycle(&vec, size)
    }

    pub fn div(&self, other: &Self) -> PyResult<Self> {
        let hset = self.na_indexes().clone();
        Ok(FloatList64::new(NumericalList::div(self, other)?, hset))
    }

    pub fn div_scala(&self, elem: f64) -> Self {
        let hset = self.na_indexes().clone();
        FloatList64::new(NumericalList::div_scala(self, elem), hset)
    }

    pub fn equal_scala(&self, elem: f64) -> BooleanList {
        List::equal_scala(self, elem)
    }

    pub fn filter(&self, condition: &BooleanList) -> PyResult<Self> {
        List::filter(self, condition)
    }

    pub fn get(&self, index: usize) -> PyResult<Option<f64>> {
        List::get(self, index)
    }

    pub fn get_by_indexes(&self, indexes: &IndexList) -> PyResult<Self> {
        List::get_by_indexes(self, indexes)
    }

    pub fn greater_than_or_equal_scala(&self, elem: f64) -> BooleanList {
        NumericalList::greater_than_or_equal_scala(self, elem)
    }

    pub fn greater_than_scala(&self, elem: f64) -> BooleanList {
        NumericalList::greater_than_scala(self, elem)
    }

    pub fn less_than_or_equal_scala(&self, elem: f64) -> BooleanList {
        NumericalList::less_than_or_equal_scala(self, elem)
    }

    pub fn less_than_scala(&self, elem: f64) -> BooleanList {
        NumericalList::less_than_scala(self, elem)
    }

    pub fn max(&self) -> PyResult<f64> {
        NumericalList::max(self)
    }

    pub fn min(&self) -> PyResult<f64> {
        NumericalList::min(self)
    }

    pub fn mul(&self, other: &Self) -> PyResult<Self> {
        NumericalList::mul(self, other)
    }

    pub fn mul_scala(&self, elem: f64) -> Self {
        NumericalList::mul_scala(self, elem)
    }

    pub fn not_equal_scala(&self, elem: f64) -> BooleanList {
        List::not_equal_scala(self, elem)
    }

    pub fn pop(&self) {
        List::pop(self);
    }

    pub fn pow_scala(&self, elem: i32) -> Self {
        NumericalList::pow_scala(self, elem)
    }

    #[staticmethod]
    pub fn repeat(elem: f64, size: usize) -> Self {
        List::repeat(elem, size)
    }

    pub fn replace(&self, old: Option<f64>, new: Option<f64>) {
        List::replace(self, old, new)
    }

    pub fn set(&self, index: usize, elem: Option<f64>) -> PyResult<()> {
        List::set(self, index, elem)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) {
        let n = self.size();
        let m = self.count_na();
        // Handle na elements.
        self._sort();
        // Sort non-na elements.
        let mut vec = self.values_mut();
        let slice = &mut vec[0..(n - m)];
        if ascending {
            slice.sort_by(|a, b| a.partial_cmp(b).unwrap());
        } else {
            slice.sort_by(|a, b| b.partial_cmp(a).unwrap());
        }
    }

    pub fn sub(&self, other: &Self) -> PyResult<Self> {
        NumericalList::sub(self, other)
    }

    pub fn sub_scala(&self, elem: f64) -> Self {
        NumericalList::sub_scala(self, elem)
    }

    pub fn sum(&self) -> f64 {
        NumericalList::sum(self)
    }

    pub fn to_list(&self) -> Vec<Option<f64>> {
        List::to_list(self)
    }

    pub fn union_all(&self, other: &Self) -> Self {
        List::union_all(self, other)
    }

    pub fn unique(&self) -> Self {
        // Get the unique values.
        let mut vec = Vec::with_capacity(self.size());
        for (i, &val) in self.values().iter().enumerate() {
            if self.na_indexes().contains(&i) {
                continue;
            }
            vec.push(val);
        }
        // Remove duplicates.
        vec.sort_by(|a, b| a.partial_cmp(b).unwrap());
        vec.dedup();
        // Copy the unique and na values to the vec.
        if self.count_na() > 0 {
            vec.push(self.na_value());
        }
        // Construct List.
        let mut hset = HashSet::new();
        if self.count_na() > 0 {
            hset.insert(vec.len() - 1);
        }
        List::_new(vec, hset)
    }
}

impl List<f64> for FloatList64 {
    fn _new(vec: Vec<f64>, hset: HashSet<usize>) -> Self {
        Self {
            _values: RefCell::new(vec),
            _na_indexes: RefCell::new(hset),
        }
    }

    fn na_indexes(&self) -> Ref<HashSet<usize>> {
        self._na_indexes.borrow()
    }

    fn na_indexes_mut(&self) -> RefMut<HashSet<usize>> {
        self._na_indexes.borrow_mut()
    }

    fn na_value(&self) -> f64 {
        0.0
    }

    fn values(&self) -> Ref<Vec<f64>> {
        self._values.borrow()
    }

    fn values_mut(&self) -> RefMut<Vec<f64>> {
        self._values.borrow_mut()
    }
}

impl NumericalList<f64, i32, f64> for FloatList64 {
    fn argmax(&self) -> PyResult<usize> {
        self._check_all_na()?;
        let vec = self.values();
        let hset = self.na_indexes();
        let val_0 = &f64::NEG_INFINITY;
        let result = vec
            .iter()
            .enumerate()
            .filter(|(i, _)| !hset.contains(i))
            .fold((0, val_0), |acc, x| if x.1 > acc.1 { x } else { acc });
        Ok(result.0)
    }

    fn argmin(&self) -> PyResult<usize> {
        self._check_all_na()?;
        let vec = self.values();
        let hset = self.na_indexes();
        let val_0 = &f64::INFINITY;
        let result = vec
            .iter()
            .enumerate()
            .filter(|(i, _)| !hset.contains(i))
            .fold((0, val_0), |acc, x| if x.1 < acc.1 { x } else { acc });
        Ok(result.0)
    }

    fn div(&self, other: &Self) -> PyResult<Vec<f64>> {
        self._check_len_eq(other)?;
        Ok(self
            .values()
            .iter()
            .zip(other.values().iter())
            .map(|(x, y)| x / y)
            .collect())
    }

    fn div_scala(&self, elem: f64) -> Vec<f64> {
        self.values().iter().map(|x| *x / elem).collect()
    }

    fn max(&self) -> PyResult<f64> {
        self._check_all_na()?;
        let hset = self.na_indexes();
        Ok(*self
            .values()
            .iter()
            .enumerate()
            .filter(|(i, _)| !hset.contains(i))
            .map(|(_, x)| x)
            .max_by(|&x, &y| x.partial_cmp(y).unwrap())
            .unwrap())
    }

    fn min(&self) -> PyResult<f64> {
        self._check_all_na()?;
        let hset = self.na_indexes();
        Ok(*self
            .values()
            .iter()
            .enumerate()
            .filter(|(i, _)| !hset.contains(i))
            .map(|(_, x)| x)
            .min_by(|&x, &y| x.partial_cmp(y).unwrap())
            .unwrap())
    }

    fn pow_scala(&self, elem: i32) -> Self {
        let vec = self.values().iter().map(|&x| x.powi(elem)).collect();
        let hset = self.na_indexes().clone();
        FloatList64::new(vec, hset)
    }

    fn sum(&self) -> f64 {
        self.values().iter().sum()
    }
}

impl AsBooleanList for FloatList64 {
    fn as_bool(&self) -> BooleanList {
        let vec = self.values().iter().map(|&x| x != 0.0).collect();
        let hset = self.na_indexes().clone();
        BooleanList::new(vec, hset)
    }
}

impl AsFloatList32 for FloatList64 {
    fn as_float32(&self) -> FloatList32 {
        let vec = self.values().iter().map(|&x| x as f32).collect();
        let hset = self.na_indexes().clone();
        FloatList32::new(vec, hset)
    }
}

impl AsIntegerList32 for FloatList64 {
    fn as_int32(&self) -> IntegerList32 {
        let vec = self.values().iter().map(|&x| x as i32).collect();
        let hset = self.na_indexes().clone();
        IntegerList32::new(vec, hset)
    }
}

impl AsIntegerList64 for FloatList64 {
    fn as_int64(&self) -> IntegerList64 {
        let vec = self.values().iter().map(|&x| x as i64).collect();
        let hset = self.na_indexes().clone();
        IntegerList64::new(vec, hset)
    }
}

impl AsStringList for FloatList64 {
    fn as_str(&self) -> StringList {
        let vec = self.values().iter().map(|&x| format!("{:?}", x)).collect();
        let hset = self.na_indexes().clone();
        StringList::new(vec, hset)
    }
}

fn _sort(vec: &mut Vec<f64>, ascending: bool) {
    if ascending {
        vec.sort_by(|a, b| a.partial_cmp(b).unwrap());
    } else {
        vec.sort_by(|a, b| b.partial_cmp(a).unwrap());
    }
}
