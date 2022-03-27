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

/// List with float type elements.
#[pyclass]
pub struct FloatList64 {
    _values: RefCell<Vec<f64>>,
}

#[pymethods]
impl FloatList64 {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<f64>) -> Self {
        List::_new(vec)
    }

    pub fn add(&self, other: &Self) -> Self {
        NumericalList::add(self, other)
    }

    pub fn add_scala(&self, elem: f64) -> Self {
        NumericalList::add_scala(self, elem)
    }

    pub fn append(&self, elem: f64) {
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

    #[staticmethod]
    pub fn cycle(vec: Vec<f64>, size: usize) -> Self {
        List::cycle(&vec, size)
    }

    pub fn div(&self, other: &Self) -> Self {
        let vec = NumericalList::div(self, other);
        FloatList64::new(vec)
    }

    pub fn div_scala(&self, elem: f64) -> Self {
        let vec = NumericalList::div_scala(self, elem);
        FloatList64::new(vec)
    }

    pub fn equal_scala(&self, elem: f64) -> BooleanList {
        List::equal_scala(self, elem)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        List::filter(self, condition)
    }

    pub fn get(&self, index: usize) -> f64 {
        List::get(self, index)
    }

    pub unsafe fn get_by_indexes(&self, indexes: &IndexList) -> Self {
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

    pub fn max(&self) -> f64 {
        NumericalList::max(self)
    }

    pub fn min(&self) -> f64 {
        NumericalList::min(self)
    }

    pub fn mul(&self, other: &Self) -> Self {
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

    pub fn replace(&self, old: f64, new: f64) -> Self {
        List::replace(self, old, new)
    }

    pub unsafe fn set(&self, index: usize, elem: f64) {
        List::set(self, index, elem)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) -> Self {
        let mut vec = self.to_list();
        let mut _vec = &mut vec;
        _sort(_vec, ascending);
        List::_new(vec)
    }

    pub fn sub(&self, other: &Self) -> Self {
        NumericalList::sub(self, other)
    }

    pub fn sub_scala(&self, elem: f64) -> Self {
        NumericalList::sub_scala(self, elem)
    }

    pub fn sum(&self) -> f64 {
        NumericalList::sum(self)
    }

    pub fn to_list(&self) -> Vec<f64> {
        List::to_list(self)
    }

    pub fn union_all(&self, other: &Self) -> Self {
        List::union_all(self, other)
    }

    pub fn unique(&self) -> Self {
        let mut vec = self.to_list();
        _sort(&mut vec, true);
        vec.dedup();
        List::_new(vec)
    }
}

impl List<f64> for FloatList64 {
    fn _new(vec: Vec<f64>) -> Self {
        Self {
            _values: RefCell::new(vec),
        }
    }

    fn values(&self) -> Ref<Vec<f64>> {
        self._values.borrow()
    }

    fn values_mut(&self) -> RefMut<Vec<f64>> {
        self._values.borrow_mut()
    }
}

impl NumericalList<f64, i32, f64> for FloatList64 {
    fn argmax(&self) -> usize {
        let mut result = (0, &self.values()[0]);
        let vec = self.values();
        for cur in vec.iter().enumerate() {
            if cur.1 > result.1 {
                result = cur;
            }
        }
        result.0
    }

    fn argmin(&self) -> usize {
        let mut result = (0, &self.values()[0]);
        let vec = self.values();
        for cur in vec.iter().enumerate() {
            if cur.1 < result.1 {
                result = cur;
            }
        }
        result.0
    }

    fn div(&self, other: &Self) -> Vec<f64> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(x, y)| x / y)
            .collect()
    }

    fn div_scala(&self, elem: f64) -> Vec<f64> {
        self.values().iter().map(|x| *x / elem).collect()
    }

    fn max(&self) -> f64 {
        *self
            .values()
            .iter()
            .max_by(|&x, &y| x.partial_cmp(y).unwrap())
            .unwrap()
    }

    fn min(&self) -> f64 {
        *self
            .values()
            .iter()
            .min_by(|&x, &y| x.partial_cmp(y).unwrap())
            .unwrap()
    }

    fn pow_scala(&self, elem: i32) -> Self {
        let vec = self.values().iter().map(|&x| x.powi(elem)).collect();
        FloatList64::new(vec)
    }

    fn sum(&self) -> f64 {
        self.values().iter().sum()
    }
}

impl AsBooleanList for FloatList64 {
    fn as_bool(&self) -> BooleanList {
        let vec = self.values().iter().map(|&x| x != 0.0).collect();
        BooleanList::new(vec)
    }
}

impl AsFloatList32 for FloatList64 {
    fn as_float32(&self) -> FloatList32 {
        let vec = self.values().iter().map(|&x| x as f32).collect();
        FloatList32::new(vec)
    }
}

impl AsIntegerList32 for FloatList64 {
    fn as_int32(&self) -> IntegerList32 {
        let vec = self.values().iter().map(|&x| x as i32).collect();
        IntegerList32::new(vec)
    }
}

impl AsIntegerList64 for FloatList64 {
    fn as_int64(&self) -> IntegerList64 {
        let vec = self.values().iter().map(|&x| x as i64).collect();
        IntegerList64::new(vec)
    }
}

impl AsStringList for FloatList64 {
    fn as_str(&self) -> StringList {
        let vec = self.values().iter().map(|&x| format!("{:?}", x)).collect();
        StringList::new(vec)
    }
}

fn _sort(vec: &mut Vec<f64>, ascending: bool) {
    if ascending {
        vec.sort_by(|a, b| a.partial_cmp(b).unwrap());
    } else {
        vec.sort_by(|a, b| b.partial_cmp(a).unwrap());
    }
}
