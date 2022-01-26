use crate::base::counter;
use crate::base::List;
use crate::boolean::BooleanList;
use crate::float::FloatList;
use crate::numerical::NumericalList;
use crate::string::StringList;
use crate::types::AsBooleanList;
use crate::types::AsFloatList;
use crate::types::AsStringList;
use pyo3::prelude::*;
use std::cell::Ref;
use std::cell::RefCell;
use std::cell::RefMut;
use std::collections::HashMap;

/// List with integer type elements.
#[pyclass]
pub struct IntegerList {
    _values: RefCell<Vec<i32>>,
}

#[pymethods]
impl IntegerList {
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

    pub fn as_float(&self) -> FloatList {
        AsFloatList::as_float(self)
    }

    pub fn as_str(&self) -> StringList {
        AsStringList::as_str(self)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn counter(&self) -> HashMap<i32, usize> {
        counter(self.values())
    }

    #[staticmethod]
    pub fn cycle(vec: Vec<i32>, size: usize) -> Self {
        List::cycle(&vec, size)
    }

    pub fn div(&self, other: &Self) -> FloatList {
        let vec = NumericalList::div(self, other);
        FloatList::new(vec)
    }

    pub fn div_scala(&self, elem: f32) -> FloatList {
        let vec = NumericalList::div_scala(self, elem);
        FloatList::new(vec)
    }

    pub fn equal_scala(&self, elem: i32) -> BooleanList {
        NumericalList::equal_scala(self, elem)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        NumericalList::filter(self, condition)
    }

    pub unsafe fn get(&self, index: usize) -> i32 {
        List::get(self, index)
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
        NumericalList::not_equal_scala(self, elem)
    }

    pub fn pop(&self) {
        List::pop(self);
    }

    pub fn pow_scala(&self, elem: u32) -> Self {
        NumericalList::pow_scala(self, elem)
    }

    pub unsafe fn set(&self, index: usize, elem: i32) {
        List::set(self, index, elem)
    }

    #[staticmethod]
    pub fn repeat(elem: i32, size: usize) -> Self {
        List::repeat(elem, size)
    }

    pub fn replace(&self, old: i32, new: i32) -> Self {
        NumericalList::replace(self, old, new)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) -> Self {
        NumericalList::sort(self, ascending)
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
        NumericalList::unique(self)
    }
}

impl List<i32> for IntegerList {
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

impl NumericalList<i32, u32> for IntegerList {
    fn _sort(&self, vec: &mut Vec<i32>, ascending: bool) {
        if ascending {
            vec.sort();
        } else {
            vec.sort_by(|a, b| b.cmp(a))
        }
    }

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

    fn div(&self, other: &Self) -> Vec<f32> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(&x, &y)| x as f32 / y as f32)
            .collect()
    }

    fn div_scala(&self, elem: f32) -> Vec<f32> {
        self.values().iter().map(|x| *x as f32 / elem).collect()
    }

    fn max(&self) -> i32 {
        *self.values().iter().max().unwrap()
    }

    fn min(&self) -> i32 {
        *self.values().iter().min().unwrap()
    }

    fn pow_scala(&self, elem: u32) -> Self {
        let vec = self.values().iter().map(|&x| x.pow(elem)).collect();
        IntegerList::new(vec)
    }

    fn sum(&self) -> i32 {
        self.values().iter().sum()
    }
}

impl AsBooleanList for IntegerList {
    fn as_bool(&self) -> BooleanList {
        let vec = self.values().iter().map(|&x| x != 0).collect();
        BooleanList::new(vec)
    }
}

impl AsFloatList for IntegerList {
    fn as_float(&self) -> FloatList {
        let vec = self.values().iter().map(|&x| x as f32).collect();
        FloatList::new(vec)
    }
}

impl AsStringList for IntegerList {
    fn as_str(&self) -> StringList {
        let vec = self.values().iter().map(|&x| x.to_string()).collect();
        StringList::new(vec)
    }
}
