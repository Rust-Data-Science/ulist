use crate::base::List;
use crate::boolean::BooleanList;
use crate::float::FloatList;
use crate::numerical::NumericalList;
use pyo3::prelude::*;
use std::cell::Ref;
use std::cell::RefCell;
use std::cell::RefMut;

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

    pub fn add_scala(&self, num: i32) -> Self {
        NumericalList::add_scala(self, num)
    }

    pub fn append(&self, num: i32) {
        List::append(self, num)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    #[staticmethod]
    pub fn cycle(vec: Vec<i32>, size: usize) -> Self {
        List::cycle(&vec, size)
    }

    pub fn div(&self, other: &Self) -> FloatList {
        let vec = NumericalList::div(self, other);
        FloatList::new(vec)
    }

    pub fn div_scala(&self, num: f32) -> FloatList {
        let vec = NumericalList::div_scala(self, num);
        FloatList::new(vec)
    }

    pub fn equal_scala(&self, num: i32) -> BooleanList {
        BooleanList::new(NumericalList::_operate_scala(self, |x| x == num))
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        NumericalList::filter(self, condition)
    }

    pub unsafe fn get(&self, index: usize) -> i32 {
        List::get(self, index)
    }

    pub fn greater_than_or_equal_scala(&self, num: i32) -> BooleanList {
        BooleanList::new(NumericalList::_operate_scala(self, |x| x >= num))
    }

    pub fn greater_than_scala(&self, num: i32) -> BooleanList {
        NumericalList::greater_than_scala(self, num)
    }

    pub fn less_than_or_equal_scala(&self, num: i32) -> BooleanList {
        BooleanList::new(NumericalList::_operate_scala(self, |x| x <= num))
    }

    pub fn less_than_scala(&self, num: i32) -> BooleanList {
        NumericalList::less_than_scala(self, num)
    }

    pub fn max(&self) -> i32 {
        NumericalList::max(self)
    }

    pub fn mean(&self) -> f32 {
        NumericalList::mean(self)
    }

    pub fn min(&self) -> i32 {
        NumericalList::min(self)
    }

    pub fn mul(&self, other: &Self) -> Self {
        NumericalList::mul(self, other)
    }

    pub fn mul_scala(&self, num: i32) -> Self {
        NumericalList::mul_scala(self, num)
    }

    pub fn not_equal_scala(&self, num: i32) -> BooleanList {
        BooleanList::new(NumericalList::_operate_scala(self, |x| x != num))
    }

    pub fn pop(&self) {
        List::pop(self);
    }

    pub fn pow_scala(&self, num: usize) -> Self {
        NumericalList::pow_scala(self, num)
    }

    pub unsafe fn set(&self, index: usize, num: i32) {
        List::set(self, index, num)
    }

    #[staticmethod]
    pub fn repeat(num: i32, size: usize) -> Self {
        List::repeat(num, size)
    }

    pub fn replace(&self, old: i32, new: i32) {
        List::replace(self, old, &new)
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

    pub fn sub_scala(&self, num: i32) -> Self {
        NumericalList::sub_scala(self, num)
    }

    pub fn sum(&self) -> i32 {
        NumericalList::sum(self)
    }

    pub fn to_list(&self) -> Vec<i32> {
        List::to_list(self)
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

impl NumericalList<i32> for IntegerList {
    fn _sort(&self, vec: &mut Vec<i32>, ascending: bool) {
        if ascending {
            vec.sort();
        } else {
            vec.sort_by(|a, b| b.cmp(a))
        }
    }

    fn div(&self, other: &Self) -> Vec<f32> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(&x, &y)| x as f32 / y as f32)
            .collect()
    }

    fn div_scala(&self, num: f32) -> Vec<f32> {
        self.values().iter().map(|x| *x as f32 / num).collect()
    }

    fn max(&self) -> i32 {
        *self.values().iter().max().unwrap()
    }

    fn min(&self) -> i32 {
        *self.values().iter().min().unwrap()
    }

    fn sum(&self) -> i32 {
        self.values().iter().sum()
    }
}
