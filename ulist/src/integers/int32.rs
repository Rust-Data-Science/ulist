use crate::base::List;
use crate::boolean::BooleanList;
use crate::floatings::FloatList32;
use crate::floatings::FloatList64;
use crate::index::IndexList;
use crate::integers::IntegerList64;
use crate::non_float::NonFloatList;
use crate::numerical::NumericalList;
use crate::string::StringList;
use crate::types::AsBooleanList;
use crate::types::AsFloatList32;
use crate::types::AsFloatList64;
use crate::types::AsIntegerList64;
use crate::types::AsStringList;
use pyo3::prelude::*;
use std::cell::Ref;
use std::cell::RefCell;
use std::cell::RefMut;
use std::collections::HashMap;

/// List with i32 type elements.
#[pyclass]
pub struct IntegerList32 {
    _values: RefCell<Vec<i32>>,
}

#[pymethods]
impl IntegerList32 {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<i32>) -> Self {
        List::_new(vec)
    }

    pub fn add(&self, other: &Self) -> Self {
        NumericalList::add(self, other)
    }

    pub fn add_scala(&self, elem: i32) -> Self {
        NumericalList::add_scala(self, elem)
    }

    pub fn append(&self, elem: i32) {
        List::append(self, elem)
    }

    pub fn argmax(&self) -> usize {
        NumericalList::argmax(self)
    }

    pub fn argmin(&self) -> usize {
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

    pub fn as_int64(&self) -> IntegerList64 {
        AsIntegerList64::as_int64(self)
    }

    pub fn as_str(&self) -> StringList {
        AsStringList::as_str(self)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn counter(&self) -> HashMap<i32, usize> {
        NonFloatList::counter(self)
    }

    #[staticmethod]
    pub fn cycle(vec: Vec<i32>, size: usize) -> Self {
        List::cycle(&vec, size)
    }

    pub fn div(&self, other: &Self) -> FloatList64 {
        let vec = NumericalList::div(self, other);
        FloatList64::new(vec)
    }

    pub fn div_scala(&self, elem: f64) -> FloatList64 {
        let vec = NumericalList::div_scala(self, elem);
        FloatList64::new(vec)
    }

    pub fn equal_scala(&self, elem: i32) -> BooleanList {
        List::equal_scala(self, elem)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        List::filter(self, condition)
    }

    pub fn get(&self, index: usize) -> i32 {
        List::get(self, index)
    }

    pub unsafe fn get_by_indexes(&self, indexes: &IndexList) -> Self {
        List::get_by_indexes(self, indexes)
    }

    pub fn greater_than_or_equal_scala(&self, elem: i32) -> BooleanList {
        NumericalList::greater_than_or_equal_scala(self, elem)
    }

    pub fn greater_than_scala(&self, elem: i32) -> BooleanList {
        NumericalList::greater_than_scala(self, elem)
    }

    pub fn less_than_or_equal_scala(&self, elem: i32) -> BooleanList {
        NumericalList::less_than_or_equal_scala(self, elem)
    }

    pub fn less_than_scala(&self, elem: i32) -> BooleanList {
        NumericalList::less_than_scala(self, elem)
    }

    pub fn max(&self) -> i32 {
        NumericalList::max(self)
    }

    pub fn min(&self) -> i32 {
        NumericalList::min(self)
    }

    pub fn mul(&self, other: &Self) -> Self {
        NumericalList::mul(self, other)
    }

    pub fn mul_scala(&self, elem: i32) -> Self {
        NumericalList::mul_scala(self, elem)
    }

    pub fn not_equal_scala(&self, elem: i32) -> BooleanList {
        List::not_equal_scala(self, elem)
    }

    pub fn pop(&self) {
        List::pop(self);
    }

    pub fn pow_scala(&self, elem: u32) -> Self {
        NumericalList::pow_scala(self, elem)
    }

    #[staticmethod]
    pub fn repeat(elem: i32, size: usize) -> Self {
        List::repeat(elem, size)
    }

    pub fn replace(&self, old: i32, new: i32) -> Self {
        List::replace(self, old, new)
    }

    pub unsafe fn set(&self, index: usize, elem: i32) {
        List::set(self, index, elem)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) -> Self {
        NonFloatList::sort(self, ascending)
    }

    pub fn sub(&self, other: &Self) -> Self {
        NumericalList::sub(self, other)
    }

    pub fn sub_scala(&self, elem: i32) -> Self {
        NumericalList::sub_scala(self, elem)
    }

    pub fn sum(&self) -> i32 {
        NumericalList::sum(self)
    }

    pub fn to_list(&self) -> Vec<i32> {
        List::to_list(self)
    }

    pub fn union_all(&self, other: &Self) -> Self {
        List::union_all(self, other)
    }

    pub fn unique(&self) -> Self {
        NonFloatList::unique(self)
    }
}

impl List<i32> for IntegerList32 {
    fn _new(vec: Vec<i32>) -> Self {
        Self {
            _values: RefCell::new(vec),
        }
    }

    fn values(&self) -> Ref<Vec<i32>> {
        self._values.borrow()
    }

    fn values_mut(&self) -> RefMut<Vec<i32>> {
        self._values.borrow_mut()
    }
}

impl NonFloatList<i32> for IntegerList32 {}

impl NumericalList<i32, u32, f64> for IntegerList32 {
    fn argmax(&self) -> usize {
        self.values()
            .iter()
            .enumerate()
            .max_by_key(|x| x.1)
            .unwrap()
            .0
    }

    fn argmin(&self) -> usize {
        self.values()
            .iter()
            .enumerate()
            .min_by_key(|x| x.1)
            .unwrap()
            .0
    }

    fn div(&self, other: &Self) -> Vec<f64> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(&x, &y)| x as f64 / y as f64)
            .collect()
    }

    fn div_scala(&self, elem: f64) -> Vec<f64> {
        self.values().iter().map(|x| *x as f64 / elem).collect()
    }

    fn max(&self) -> i32 {
        *self.values().iter().max().unwrap()
    }

    fn min(&self) -> i32 {
        *self.values().iter().min().unwrap()
    }

    fn pow_scala(&self, elem: u32) -> Self {
        let vec = self.values().iter().map(|&x| x.pow(elem)).collect();
        IntegerList32::new(vec)
    }

    fn sum(&self) -> i32 {
        self.values().iter().sum()
    }
}

impl AsBooleanList for IntegerList32 {
    fn as_bool(&self) -> BooleanList {
        let vec = self.values().iter().map(|&x| x != 0).collect();
        BooleanList::new(vec)
    }
}

impl AsFloatList32 for IntegerList32 {
    fn as_float32(&self) -> FloatList32 {
        let vec = self.values().iter().map(|&x| x as f32).collect();
        FloatList32::new(vec)
    }
}

impl AsFloatList64 for IntegerList32 {
    fn as_float64(&self) -> FloatList64 {
        let vec = self.values().iter().map(|&x| x as f64).collect();
        FloatList64::new(vec)
    }
}

impl AsIntegerList64 for IntegerList32 {
    fn as_int64(&self) -> IntegerList64 {
        let vec = self.values().iter().map(|&x| x as i64).collect();
        IntegerList64::new(vec)
    }
}

impl AsStringList for IntegerList32 {
    fn as_str(&self) -> StringList {
        let vec = self.values().iter().map(|&x| x.to_string()).collect();
        StringList::new(vec)
    }
}
