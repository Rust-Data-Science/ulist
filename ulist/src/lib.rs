mod list;
use list::BooleanList;
use list::List;
use pyo3::class::sequence::PySequenceProtocol;
use pyo3::prelude::*;

/// List for f32.
#[pyclass]
struct FloatList {
    _list: Vec<f32>,
}

#[pymethods]
impl FloatList {
    #[new]
    fn new(list: Vec<f32>) -> Self {
        List::_new(list)
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
        let list = List::div(self, other);
        List::_new(list)
    }

    pub fn div_scala(&self, num: f32) -> Self {
        let list = List::div_scala(self, num);
        List::_new(list)
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
    fn _new(list: Vec<f32>) -> Self {
        Self { _list: list }
    }

    fn _sort(&self, list: &mut Vec<f32>, ascending: bool) {
        if ascending {
            list.sort_by(|a, b| a.partial_cmp(b).unwrap());
        } else {
            list.sort_by(|a, b| b.partial_cmp(a).unwrap());
        }
    }

    fn _values(&'a self) -> &'a Vec<f32> {
        &self._list
    }

    fn div(&'a self, other: &Self) -> Vec<f32> {
        self._values()
            .iter()
            .zip(other._values().iter())
            .map(|(x, y)| x / y)
            .collect()
    }

    fn div_scala(&'a self, num: f32) -> Vec<f32> {
        self._values().iter().map(|x| *x / num).collect()
    }

    fn max(&'a self) -> f32 {
        self._values()
            .iter()
            .fold(f32::NEG_INFINITY, |x, &y| x.max(y))
    }

    fn min(&'a self) -> f32 {
        self._values().iter().fold(f32::INFINITY, |x, &y| x.min(y))
    }
}

#[pyproto]
impl PySequenceProtocol for FloatList {
    fn __len__(&self) -> usize {
        self.size()
    }
}

/// List for i32.
#[pyclass]
struct IntegerList {
    _list: Vec<i32>,
}

#[pymethods]
impl IntegerList {
    #[new]
    fn new(list: Vec<i32>) -> Self {
        List::_new(list)
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
        let list = List::div(self, other);
        List::_new(list)
    }

    pub fn div_scala(&self, num: f32) -> FloatList {
        let list = List::div_scala(self, num);
        List::_new(list)
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
    fn _new(list: Vec<i32>) -> Self {
        Self { _list: list }
    }

    fn _sort(&self, list: &mut Vec<i32>, ascending: bool) {
        if ascending {
            list.sort();
        } else {
            list.sort_by(|a, b| b.cmp(a))
        }
    }

    fn _values(&'a self) -> &'a Vec<i32> {
        &self._list
    }

    fn div(&'a self, other: &'a Self) -> Vec<f32> {
        self._values()
            .iter()
            .zip(other._values().iter())
            .map(|(&x, &y)| x as f32 / y as f32)
            .collect()
    }

    fn div_scala(&'a self, num: f32) -> Vec<f32> {
        self._values().iter().map(|x| *x as f32 / num).collect()
    }

    fn max(&'a self) -> i32 {
        *self._values().iter().max().unwrap()
    }

    fn min(&'a self) -> i32 {
        *self._values().iter().min().unwrap()
    }
}

#[pyproto]
impl PySequenceProtocol for IntegerList {
    fn __len__(&self) -> usize {
        self.size()
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
