use crate::base::List;
use crate::boolean::BooleanList;
use crate::integer::IntegerList;
use crate::numerical::NumericalList;
use crate::string::StringList;
use crate::types::AsBooleanList;
use crate::types::AsIntegerList;
use crate::types::AsStringList;
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

    pub fn add_scala(&self, elem: f32) -> Self {
        NumericalList::add_scala(self, elem)
    }

    pub fn append(&self, elem: f32) {
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

    pub fn as_int(&self) -> IntegerList {
        AsIntegerList::as_int(self)
    }

    pub fn as_str(&self) -> StringList {
        AsStringList::as_str(self)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    #[staticmethod]
    pub fn cycle(vec: Vec<f32>, size: usize) -> Self {
        List::cycle(&vec, size)
    }

    pub fn div(&self, other: &Self) -> Self {
        let vec = NumericalList::div(self, other);
        FloatList::new(vec)
    }

    pub fn div_scala(&self, elem: f32) -> Self {
        let vec = NumericalList::div_scala(self, elem);
        FloatList::new(vec)
    }

    pub fn equal_scala(&self, elem: f32) -> BooleanList {
        List::equal_scala(self, elem)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        List::filter(self, condition)
    }

    pub unsafe fn get(&self, index: usize) -> f32 {
        List::get(self, index)
    }

    pub fn greater_than_or_equal_scala(&self, elem: f32) -> BooleanList {
        NumericalList::greater_than_or_equal_scala(self, elem)
    }

    pub fn greater_than_scala(&self, elem: f32) -> BooleanList {
        NumericalList::greater_than_scala(self, elem)
    }

    pub fn less_than_or_equal_scala(&self, elem: f32) -> BooleanList {
        NumericalList::less_than_or_equal_scala(self, elem)
    }

    pub fn less_than_scala(&self, elem: f32) -> BooleanList {
        NumericalList::less_than_scala(self, elem)
    }

    pub fn max(&self) -> f32 {
        NumericalList::max(self)
    }

    pub fn min(&self) -> f32 {
        NumericalList::min(self)
    }

    pub fn mul(&self, other: &Self) -> Self {
        NumericalList::mul(self, other)
    }

    pub fn mul_scala(&self, elem: f32) -> Self {
        NumericalList::mul_scala(self, elem)
    }

    pub fn not_equal_scala(&self, elem: f32) -> BooleanList {
        List::not_equal_scala(self, elem)
    }

    pub fn pop(&self) {
        List::pop(self);
    }

    pub fn pow_scala(&self, elem: i32) -> Self {
        NumericalList::pow_scala(self, elem)
    }

    #[staticmethod]
    pub fn repeat(elem: f32, size: usize) -> Self {
        List::repeat(elem, size)
    }

    pub fn replace(&self, old: f32, new: f32) -> Self {
        List::replace(self, old, new)
    }

    pub unsafe fn set(&self, index: usize, elem: f32) {
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

    pub fn sub_scala(&self, elem: f32) -> Self {
        NumericalList::sub_scala(self, elem)
    }

    pub fn sum(&self) -> f32 {
        NumericalList::sum(self)
    }

    pub fn to_list(&self) -> Vec<f32> {
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

impl NumericalList<f32, i32> for FloatList {
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

    fn div(&self, other: &Self) -> Vec<f32> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(x, y)| x / y)
            .collect()
    }

    fn div_scala(&self, elem: f32) -> Vec<f32> {
        self.values().iter().map(|x| *x / elem).collect()
    }

    fn max(&self) -> f32 {
        *self
            .values()
            .iter()
            .max_by(|&x, &y| x.partial_cmp(y).unwrap())
            .unwrap()
    }

    fn min(&self) -> f32 {
        *self
            .values()
            .iter()
            .min_by(|&x, &y| x.partial_cmp(y).unwrap())
            .unwrap()
    }

    fn pow_scala(&self, elem: i32) -> Self {
        let vec = self.values().iter().map(|&x| x.powi(elem)).collect();
        FloatList::new(vec)
    }

    fn sum(&self) -> f32 {
        self.values().iter().sum()
    }
}

impl AsBooleanList for FloatList {
    fn as_bool(&self) -> BooleanList {
        let vec = self.values().iter().map(|&x| x != 0.0).collect();
        BooleanList::new(vec)
    }
}

impl AsIntegerList for FloatList {
    fn as_int(&self) -> IntegerList {
        let vec = self.values().iter().map(|&x| x as i32).collect();
        IntegerList::new(vec)
    }
}

impl AsStringList for FloatList {
    fn as_str(&self) -> StringList {
        let vec = self.values().iter().map(|&x| format!("{:?}", x)).collect();
        StringList::new(vec)
    }
}

fn _sort(vec: &mut Vec<f32>, ascending: bool) {
    if ascending {
        vec.sort_by(|a, b| a.partial_cmp(b).unwrap());
    } else {
        vec.sort_by(|a, b| b.partial_cmp(a).unwrap());
    }
}
