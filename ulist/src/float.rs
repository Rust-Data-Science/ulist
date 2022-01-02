use crate::base::List;
use crate::boolean::BooleanList;
use crate::numerical::NumericalList;
use pyo3::prelude::*;
use std::cell::Ref;
use std::cell::RefCell;
use std::cell::RefMut;

/// List with float type elements.
#[pyclass]
pub struct FloatList {
    _values: RefCell<Vec<f32>>,
}

#[pymethods]
impl FloatList {
    // Arrange the following methods in alphabetical order.

    #[new]
    pub fn new(vec: Vec<f32>) -> Self {
        List::_new(vec)
    }

    pub fn add(&self, other: &Self) -> Self {
        NumericalList::add(self, other)
    }

    pub fn add_scala(&self, num: f32) -> Self {
        NumericalList::add_scala(self, num)
    }

    pub fn append(&self, num: f32) {
        List::append(self, num)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn div(&self, other: &Self) -> Self {
        let vec = NumericalList::div(self, other);
        FloatList::new(vec)
    }

    pub fn div_scala(&self, num: f32) -> Self {
        let vec = NumericalList::div_scala(self, num);
        FloatList::new(vec)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        NumericalList::filter(self, condition)
    }

    pub unsafe fn get(&self, index: usize) -> f32 {
        List::get(self, index)
    }

    pub fn greater_than_scala(&self, num: f32) -> BooleanList {
        NumericalList::greater_than_scala(self, num)
    }

    pub fn less_than_scala(&self, num: f32) -> BooleanList {
        NumericalList::less_than_scala(self, num)
    }

    pub fn max(&self) -> f32 {
        NumericalList::max(self)
    }

    pub fn mean(&self) -> f32 {
        NumericalList::mean(self)
    }

    pub fn min(&self) -> f32 {
        NumericalList::min(self)
    }

    pub fn mul(&self, other: &Self) -> Self {
        NumericalList::mul(self, other)
    }

    pub fn mul_scala(&self, num: f32) -> Self {
        NumericalList::mul_scala(self, num)
    }

    pub fn pop(&self) {
        List::pop(self);
    }

    pub fn pow_scala(&self, num: usize) -> Self {
        NumericalList::pow_scala(self, num)
    }

    pub fn replace(&self, old: f32, new: f32) {
        List::replace(self, old, &new)
    }

    pub unsafe fn set(&self, index: usize, num: f32) {
        List::set(self, index, num)
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

    pub fn sub_scala(&self, num: f32) -> Self {
        NumericalList::sub_scala(self, num)
    }

    pub fn sum(&self) -> f32 {
        NumericalList::sum(self)
    }

    pub fn to_list(&self) -> Vec<f32> {
        List::to_list(self)
    }

    pub fn unique(&self) -> Self {
        NumericalList::unique(self)
    }
}

impl List<f32> for FloatList {
    fn _new(vec: Vec<f32>) -> Self {
        Self {
            _values: RefCell::new(vec),
        }
    }

    fn values(&self) -> Ref<Vec<f32>> {
        self._values.borrow()
    }

    fn values_mut(&self) -> RefMut<Vec<f32>> {
        self._values.borrow_mut()
    }
}

impl NumericalList<f32> for FloatList {
    fn _sort(&self, vec: &mut Vec<f32>, ascending: bool) {
        if ascending {
            vec.sort_by(|a, b| a.partial_cmp(b).unwrap());
        } else {
            vec.sort_by(|a, b| b.partial_cmp(a).unwrap());
        }
    }

    fn div(&self, other: &Self) -> Vec<f32> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(x, y)| x / y)
            .collect()
    }

    fn div_scala(&self, num: f32) -> Vec<f32> {
        self.values().iter().map(|x| *x / num).collect()
    }

    fn max(&self) -> f32 {
        self.values()
            .iter()
            .fold(f32::NEG_INFINITY, |x, &y| x.max(y))
    }

    fn min(&self) -> f32 {
        self.values().iter().fold(f32::INFINITY, |x, &y| x.min(y))
    }

    fn sum(&self) -> f32 {
        self.values().iter().sum()
    }
}