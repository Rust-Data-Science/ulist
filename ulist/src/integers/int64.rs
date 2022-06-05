use crate::base::List;
use crate::boolean::BooleanList;
use crate::floatings::FloatList32;
use crate::floatings::FloatList64;
use crate::index::IndexList;
use crate::integers::IntegerList32;
use crate::non_float::NonFloatList;
use crate::numerical::NumericalList;
use crate::string::StringList;
use crate::types::AsBooleanList;
use crate::types::AsFloatList32;
use crate::types::AsFloatList64;
use crate::types::AsIntegerList32;
use crate::types::AsStringList;
use pyo3::prelude::*;
use std::cell::Ref;
use std::cell::RefCell;
use std::cell::RefMut;
use std::collections::HashMap;
use std::collections::HashSet;

/// List with i64 type elements.
/// TODO: Use macro to generate codes by using IntegerList32's
/// implementation
#[pyclass]
pub struct IntegerList64 {
    _values: RefCell<Vec<i64>>,
    _na_indexes: RefCell<HashSet<usize>>,
}

#[pymethods]
impl IntegerList64 {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<i64>, hset: HashSet<usize>) -> Self {
        List::_new(vec, hset)
    }

    pub fn add(&self, other: &Self) -> PyResult<Self> {
        NumericalList::add(self, other)
    }

    pub fn add_scala(&self, elem: i64) -> Self {
        NumericalList::add_scala(self, elem)
    }

    pub fn all_equal(&self, other: &Self) -> Option<bool> {
        List::all_equal(self, other)
    }

    pub fn append(&self, elem: Option<i64>) {
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

    pub fn as_float64(&self) -> FloatList64 {
        AsFloatList64::as_float64(self)
    }

    pub fn as_int32(&self) -> IntegerList32 {
        AsIntegerList32::as_int32(self)
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

    pub fn counter(&self) -> HashMap<i64, usize> {
        NonFloatList::counter(self)
    }

    #[staticmethod]
    pub fn cycle(vec: Vec<i64>, size: usize) -> Self {
        List::cycle(&vec, size)
    }

    pub fn div(&self, other: &Self) -> PyResult<FloatList64> {
        let hset: HashSet<usize> = self
            .na_indexes()
            .iter()
            .chain(other.na_indexes().iter())
            .copied()
            .collect();
        Ok(FloatList64::new(NumericalList::div(self, other)?, hset))
    }

    pub fn div_scala(&self, elem: f64) -> FloatList64 {
        let hset = self.na_indexes().clone();
        FloatList64::new(NumericalList::div_scala(self, elem), hset)
    }

    pub fn equal(&self, other: &Self) -> PyResult<BooleanList> {
        List::equal(self, other)
    }

    pub fn equal_scala(&self, elem: i64) -> BooleanList {
        List::equal_scala(self, elem)
    }

    pub fn filter(&self, condition: &BooleanList) -> PyResult<Self> {
        List::filter(self, condition)
    }

    pub fn get(&self, index: usize) -> PyResult<Option<i64>> {
        List::get(self, index)
    }

    pub fn get_by_indexes(&self, indexes: &IndexList) -> PyResult<Self> {
        List::get_by_indexes(self, indexes)
    }

    pub fn greater_than_or_equal(&self, other: &Self) -> PyResult<BooleanList> {
        NumericalList::greater_than_or_equal(self, other)
    }

    pub fn greater_than_or_equal_scala(&self, elem: i64) -> BooleanList {
        NumericalList::greater_than_or_equal_scala(self, elem)
    }

    pub fn greater_than(&self, other: &Self) -> PyResult<BooleanList> {
        NumericalList::greater_than(self, other)
    }

    pub fn greater_than_scala(&self, elem: i64) -> BooleanList {
        NumericalList::greater_than_scala(self, elem)
    }

    pub fn less_than_or_equal(&self, other: &Self) -> PyResult<BooleanList> {
        NumericalList::less_than_or_equal(self, other)
    }

    pub fn less_than_or_equal_scala(&self, elem: i64) -> BooleanList {
        NumericalList::less_than_or_equal_scala(self, elem)
    }

    pub fn less_than(&self, other: &Self) -> PyResult<BooleanList> {
        NumericalList::less_than(self, other)
    }

    pub fn less_than_scala(&self, elem: i64) -> BooleanList {
        NumericalList::less_than_scala(self, elem)
    }

    pub fn max(&self) -> PyResult<i64> {
        NumericalList::max(self)
    }

    pub fn min(&self) -> PyResult<i64> {
        NumericalList::min(self)
    }

    pub fn mul(&self, other: &Self) -> PyResult<Self> {
        NumericalList::mul(self, other)
    }

    pub fn mul_scala(&self, elem: i64) -> Self {
        NumericalList::mul_scala(self, elem)
    }

    pub fn not_equal(&self, other: &Self) -> PyResult<BooleanList> {
        List::not_equal(self, other)
    }

    pub fn not_equal_scala(&self, elem: i64) -> BooleanList {
        List::not_equal_scala(self, elem)
    }

    pub fn pop(&self) {
        List::pop(self);
    }

    pub fn pow_scala(&self, elem: u32) -> Self {
        NumericalList::pow_scala(self, elem)
    }

    #[staticmethod]
    pub fn repeat(elem: i64, size: usize) -> Self {
        List::repeat(elem, size)
    }

    pub fn replace(&self, old: Option<i64>, new: Option<i64>) {
        List::replace(self, old, new)
    }

    pub fn set(&self, index: usize, elem: Option<i64>) -> PyResult<()> {
        List::set(self, index, elem)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) {
        NonFloatList::sort(self, ascending)
    }

    pub fn sub(&self, other: &Self) -> PyResult<Self> {
        NumericalList::sub(self, other)
    }

    pub fn sub_scala(&self, elem: i64) -> Self {
        NumericalList::sub_scala(self, elem)
    }

    pub fn sum(&self) -> i64 {
        NumericalList::sum(self)
    }

    pub fn to_list(&self) -> Vec<Option<i64>> {
        List::to_list(self)
    }

    pub fn union_all(&self, other: &Self) -> Self {
        List::union_all(self, other)
    }

    pub fn unique(&self) -> Self {
        NonFloatList::unique(self)
    }
}

impl List<i64> for IntegerList64 {
    fn _new(vec: Vec<i64>, hset: HashSet<usize>) -> Self {
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

    fn na_value(&self) -> i64 {
        0
    }

    fn values(&self) -> Ref<Vec<i64>> {
        self._values.borrow()
    }

    fn values_mut(&self) -> RefMut<Vec<i64>> {
        self._values.borrow_mut()
    }
}

impl NonFloatList<i64> for IntegerList64 {}

impl NumericalList<i64, u32, f64> for IntegerList64 {
    fn argmax(&self) -> PyResult<usize> {
        self._check_all_na()?;
        let hset = self.na_indexes();
        Ok(self
            .values()
            .iter()
            .enumerate()
            .filter(|(i, _)| !hset.contains(i))
            .max_by_key(|x| x.1)
            .unwrap()
            .0)
    }

    fn argmin(&self) -> PyResult<usize> {
        self._check_all_na()?;
        let hset = self.na_indexes();
        Ok(self
            .values()
            .iter()
            .enumerate()
            .filter(|(i, _)| !hset.contains(i))
            .min_by_key(|x| x.1)
            .unwrap()
            .0)
    }

    fn div(&self, other: &Self) -> PyResult<Vec<f64>> {
        self._check_len_eq(other)?;
        let hset1 = self.na_indexes();
        let hset2 = other.na_indexes();
        Ok(self
            .values()
            .iter()
            .enumerate()
            .zip(other.values().iter())
            .map(|((i, &x), &y)| {
                if hset1.contains(&i) | hset2.contains(&i) {
                    0.0
                } else {
                    x as f64 / y as f64
                }
            })
            .collect())
    }

    fn div_scala(&self, elem: f64) -> Vec<f64> {
        self.values().iter().map(|x| *x as f64 / elem).collect()
    }

    fn max(&self) -> PyResult<i64> {
        self._check_all_na()?;
        let hset = self.na_indexes();
        Ok(*self
            .values()
            .iter()
            .enumerate()
            .filter(|(i, _)| !hset.contains(i))
            .map(|(_, x)| x)
            .max()
            .unwrap())
    }

    fn min(&self) -> PyResult<i64> {
        self._check_all_na()?;
        let hset = self.na_indexes();
        Ok(*self
            .values()
            .iter()
            .enumerate()
            .filter(|(i, _)| !hset.contains(i))
            .map(|(_, x)| x)
            .min()
            .unwrap())
    }

    fn pow_scala(&self, elem: u32) -> Self {
        let vec = self.values().iter().map(|&x| x.pow(elem)).collect();
        let hset = self.na_indexes().clone();
        IntegerList64::new(vec, hset)
    }

    fn sum(&self) -> i64 {
        self.values().iter().sum()
    }
}

impl AsBooleanList for IntegerList64 {
    fn as_bool(&self) -> BooleanList {
        let vec = self.values().iter().map(|&x| x != 0).collect();
        let hset = self.na_indexes().clone();
        BooleanList::new(vec, hset)
    }
}

impl AsFloatList32 for IntegerList64 {
    fn as_float32(&self) -> FloatList32 {
        let vec = self.values().iter().map(|&x| x as f32).collect();
        let hset = self.na_indexes().clone();
        FloatList32::new(vec, hset)
    }
}

impl AsFloatList64 for IntegerList64 {
    fn as_float64(&self) -> FloatList64 {
        let vec = self.values().iter().map(|&x| x as f64).collect();
        let hset = self.na_indexes().clone();
        FloatList64::new(vec, hset)
    }
}

impl AsIntegerList32 for IntegerList64 {
    fn as_int32(&self) -> IntegerList32 {
        let vec = self.values().iter().map(|&x| x as i32).collect();
        let hset = self.na_indexes().clone();
        IntegerList32::new(vec, hset)
    }
}

impl AsStringList for IntegerList64 {
    fn as_str(&self) -> StringList {
        let vec = self.values().iter().map(|&x| x.to_string()).collect();
        let hset = self.na_indexes().clone();
        StringList::new(vec, hset)
    }
}
