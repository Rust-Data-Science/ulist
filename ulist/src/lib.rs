mod list;
use list::BooleanList;
use list::List;
use pyo3::prelude::*;

/// List for f32.
#[pyclass]
struct FloatList {
    _values: Vec<f32>,
}

#[pymethods]
impl FloatList {
    #[new]
    fn new(vec: Vec<f32>) -> Self {
        List::_new(vec)
    }

    pub fn add(&self, other: &Self) -> Self {
        List::add(self, other)
    }

    pub fn add_scala(&self, num: f32) -> Self {
        List::add_scala(self, num)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn div(&self, other: &Self) -> Self {
        let vec = List::div(self, other);
        List::_new(vec)
    }

    pub fn div_scala(&self, num: f32) -> Self {
        let vec = List::div_scala(self, num);
        List::_new(vec)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        List::filter(self, condition)
    }

    pub fn max(&self) -> f32 {
        List::max(self)
    }

    pub fn mean(&self) -> f32 {
        List::mean(self)
    }

    pub fn min(&self) -> f32 {
        List::min(self)
    }

    pub fn mul(&self, other: &Self) -> Self {
        List::mul(self, other)
    }

    pub fn mul_scala(&self, num: f32) -> Self {
        List::mul_scala(self, num)
    }

    pub fn pow_scala(&self, num: usize) -> Self {
        List::pow_scala(self, num)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) -> Self {
        List::sort(self, ascending)
    }

    pub fn sub(&self, other: &Self) -> Self {
        List::sub(self, other)
    }

    pub fn sub_scala(&self, num: f32) -> Self {
        List::sub_scala(self, num)
    }

    pub fn sum(&self) -> f32 {
        List::sum(self)
    }

    pub fn to_list(&self) -> Vec<f32> {
        List::to_list(self)
    }

    pub fn unique(&self) -> Self {
        List::unique(self)
    }
}

impl<'a> List<'a, f32> for FloatList {
    fn _new(vec: Vec<f32>) -> Self {
        Self { _values: vec }
    }

    fn _sort(&self, vec: &mut Vec<f32>, ascending: bool) {
        if ascending {
            vec.sort_by(|a, b| a.partial_cmp(b).unwrap());
        } else {
            vec.sort_by(|a, b| b.partial_cmp(a).unwrap());
        }
    }

    fn values(&'a self) -> &'a Vec<f32> {
        &self._values
    }

    fn div(&'a self, other: &Self) -> Vec<f32> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(x, y)| x / y)
            .collect()
    }

    fn div_scala(&'a self, num: f32) -> Vec<f32> {
        self.values().iter().map(|x| *x / num).collect()
    }

    fn max(&'a self) -> f32 {
        self.values()
            .iter()
            .fold(f32::NEG_INFINITY, |x, &y| x.max(y))
    }

    fn min(&'a self) -> f32 {
        self.values().iter().fold(f32::INFINITY, |x, &y| x.min(y))
    }
}

/// List for i32.
#[pyclass]
struct IntegerList {
    _values: Vec<i32>,
}

#[pymethods]
impl IntegerList {
    #[new]
    fn new(vec: Vec<i32>) -> Self {
        List::_new(vec)
    }

    pub fn add(&self, other: &Self) -> Self {
        List::add(self, other)
    }

    pub fn add_scala(&self, num: i32) -> Self {
        List::add_scala(self, num)
    }

    pub fn copy(&self) -> Self {
        List::copy(self)
    }

    pub fn div(&self, other: &Self) -> FloatList {
        let vec = List::div(self, other);
        List::_new(vec)
    }

    pub fn div_scala(&self, num: f32) -> FloatList {
        let vec = List::div_scala(self, num);
        List::_new(vec)
    }

    pub fn filter(&self, condition: &BooleanList) -> Self {
        List::filter(self, condition)
    }

    pub fn max(&self) -> i32 {
        List::max(self)
    }

    pub fn mean(&self) -> f32 {
        List::mean(self)
    }

    pub fn min(&self) -> i32 {
        List::min(self)
    }

    pub fn mul(&self, other: &Self) -> Self {
        List::mul(self, other)
    }

    pub fn mul_scala(&self, num: i32) -> Self {
        List::mul_scala(self, num)
    }

    pub fn pow_scala(&self, num: usize) -> Self {
        List::pow_scala(self, num)
    }

    pub fn size(&self) -> usize {
        List::size(self)
    }

    pub fn sort(&self, ascending: bool) -> Self {
        List::sort(self, ascending)
    }

    pub fn sub(&self, other: &Self) -> Self {
        List::sub(self, other)
    }

    pub fn sub_scala(&self, num: i32) -> Self {
        List::sub_scala(self, num)
    }

    pub fn sum(&self) -> i32 {
        List::sum(self)
    }

    pub fn to_list(&self) -> Vec<i32> {
        List::to_list(self)
    }

    pub fn unique(&self) -> Self {
        List::unique(self)
    }
}

impl<'a> List<'a, i32> for IntegerList {
    fn _new(vec: Vec<i32>) -> Self {
        Self { _values: vec }
    }

    fn _sort(&self, vec: &mut Vec<i32>, ascending: bool) {
        if ascending {
            vec.sort();
        } else {
            vec.sort_by(|a, b| b.cmp(a))
        }
    }

    fn values(&'a self) -> &'a Vec<i32> {
        &self._values
    }

    fn div(&'a self, other: &'a Self) -> Vec<f32> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(&x, &y)| x as f32 / y as f32)
            .collect()
    }

    fn div_scala(&'a self, num: f32) -> Vec<f32> {
        self.values().iter().map(|x| *x as f32 / num).collect()
    }

    fn max(&'a self) -> i32 {
        *self.values().iter().max().unwrap()
    }

    fn min(&'a self) -> i32 {
        *self.values().iter().min().unwrap()
    }
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn ulist(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<FloatList>()?;
    m.add_class::<IntegerList>()?;
    m.add_class::<BooleanList>()?;

    Ok(())
}
