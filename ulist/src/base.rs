use crate::boolean::BooleanList;
use crate::index::IndexList;
use pyo3::exceptions::PyIndexError;
use pyo3::exceptions::PyRuntimeError;
use pyo3::PyResult;
use std::cell::Ref;
use std::cell::RefMut;
use std::collections::HashSet;

pub fn _fill_na<T: Clone>(vec: &mut [T], na_indexes: Ref<HashSet<usize>>, na_value: T) {
    for i in na_indexes.iter() {
        let ptr = unsafe { vec.get_unchecked_mut(*i) };
        *ptr = na_value.clone();
    }
}

/// Abstract List with generic type elements.
pub trait List<T>
where
    T: PartialEq + Clone,
    Self: Sized,
{
    // Arrange the following methods in alphabetical order.

    fn _new(vec: Vec<T>, hset: HashSet<usize>) -> Self;

    fn _check_len_eq(&self, other: &Self) -> PyResult<()> {
        if self.size() != other.size() {
            Err(PyRuntimeError::new_err(
                "The sizes of `self` and `other` should be equal!",
            ))
        } else {
            Ok(())
        }
    }

    // TODO: Better abstraction for List::_cmp and NumericalList::_fn methods.
    fn _cmp(&self, other: &Self, func: impl Fn(T, T) -> bool) -> PyResult<BooleanList> {
        self._check_len_eq(other)?;
        let vec = self
            .values()
            .iter()
            .zip(other.values().iter())
            .map(|(x, y)| func(x.clone(), y.clone()))
            .collect();
        let hset: HashSet<usize> = self
            .na_indexes()
            .iter()
            .chain(other.na_indexes().iter())
            .copied()
            .collect();
        let result = BooleanList::_new(vec, hset);
        _fill_na(&mut result.values_mut(), result.na_indexes(), false);
        Ok(result)
    }

    fn _fn_scala<U>(&self, func: impl Fn(&T) -> U) -> Vec<U> {
        self.values().iter().map(func).collect()
    }

    fn _sort(&self) {
        let n = self.size();
        let m = self.count_na();
        if m == n {
            return;
        }
        let mut vec = self.values_mut();
        let mut hset = self.na_indexes_mut();
        // Put all the na elements to the right side.
        let mut l = 0;
        let mut r = n - 1;
        while l < r && !hset.is_empty() {
            while l < r && !hset.contains(&l) {
                l += 1;
            }
            while l < r && hset.contains(&r) {
                r -= 1;
            }
            vec.swap(l, r);
            hset.remove(&l);
            hset.insert(r);
        }
    }

    fn all_equal(&self, other: &Self) -> Option<bool> {
        if self.size() != other.size() {
            return Some(false);
        };
        let hset1 = self.na_indexes();
        let hset2 = other.na_indexes();
        let mut result = Some(true);
        for (i, (x1, x2)) in self.values().iter().zip(other.values().iter()).enumerate() {
            if hset1.contains(&i) || hset2.contains(&i) {
                result = None;
            } else if x1 != x2 {
                return Some(false);
            }
        }
        result
    }

    fn append(&self, elem: Option<T>) {
        if let Some(i) = elem {
            self.values_mut().push(i);
        } else {
            self.na_indexes_mut().insert(self.size());
            self.values_mut().push(self.na_value());
        }
    }

    fn copy(&self) -> Self {
        let hset = self.na_indexes().clone();
        List::_new(self.values().clone(), hset)
    }

    fn count_na(&self) -> usize {
        self.na_indexes().len()
    }

    fn cycle(vec: &[T], size: usize) -> Self {
        let v: Vec<_> = vec.iter().cycle().take(size).cloned().collect();
        List::_new(v, HashSet::new())
    }

    fn equal(&self, other: &Self) -> PyResult<BooleanList> {
        self._cmp(other, |x, y| x == y)
    }

    fn equal_scala(&self, elem: T) -> BooleanList {
        let mut vec = self._fn_scala(|x| x == &elem);
        _fill_na(&mut vec, self.na_indexes(), false);
        let hset = self.na_indexes().clone();
        BooleanList::new(vec, hset)
    }

    fn filter(&self, condition: &BooleanList) -> PyResult<Self> {
        if self.size() != condition.size() {
            return Err(PyRuntimeError::new_err(
                "The sizes of `self` and `other` should be equal!",
            ));
        }

        let n = self.size();
        let m = self.count_na();
        let mut vec: Vec<T> = Vec::with_capacity(n);
        let mut hset: HashSet<usize> = HashSet::with_capacity(m);
        let cond = condition.values();
        let mut i = 0;
        for ((j, x), cond) in self.values().iter().enumerate().zip(cond.iter()) {
            if *cond {
                // TODO: Use get_unchecked_mut instead
                // let ptr = unsafe { vec.get_unchecked_mut(i) };
                // *ptr = x.clone();
                vec.push(x.clone());
                if self.na_indexes().contains(&j) {
                    hset.insert(i);
                }
                i += 1;
            }
        }
        vec.shrink_to_fit();
        hset.shrink_to_fit();
        Ok(List::_new(vec, hset))
    }

    fn get(&self, index: usize) -> PyResult<Option<T>> {
        if self.na_indexes().contains(&index) {
            return Ok(None);
        }
        let vec = self.values();
        let val = vec.get(index);
        if let Some(i) = val {
            Ok(Some(i.clone()))
        } else {
            Err(PyIndexError::new_err("Index out of range!"))
        }
    }

    fn get_by_indexes(&self, indexes: &IndexList) -> PyResult<Self> {
        // TODO: Put this kind of check
        // where there is unsafe block.
        if indexes.back() >= self.size() {
            return Err(PyIndexError::new_err("Index out of range!"));
        }
        // TODO: use get_unchecked instead.
        let mut vec: Vec<T> = Vec::new();
        let mut hset: HashSet<usize> = HashSet::new();
        for (i, j) in indexes.values().iter().enumerate() {
            vec.push(self.values()[*j].clone());
            if self.na_indexes().contains(j) {
                hset.insert(i);
            }
        }
        Ok(List::_new(vec, hset))
    }

    fn na_indexes(&self) -> Ref<HashSet<usize>>;

    fn na_indexes_mut(&self) -> RefMut<HashSet<usize>>;

    fn na_value(&self) -> T;

    fn not_equal(&self, other: &Self) -> PyResult<BooleanList> {
        self._cmp(other, |x, y| x != y)
    }

    fn not_equal_scala(&self, elem: T) -> BooleanList {
        let mut vec = self._fn_scala(|x| x != &elem);
        _fill_na(&mut vec, self.na_indexes(), false);
        let hset = self.na_indexes().clone();
        BooleanList::new(vec, hset)
    }

    fn pop(&self) {
        let i = self.size() - 1;
        if self.na_indexes().contains(&i) {
            self.na_indexes_mut().remove(&i);
        }
        self.values_mut().pop();
    }

    // TODO: Test if old does not exist in self.
    fn replace(&self, old: Option<T>, new: Option<T>) {
        if let Some(_old) = old {
            if let Some(_new) = new {
                self.replace_elem(_old, _new)
            } else {
                self.replace_by_na(_old)
            }
        } else if let Some(_new) = new {
            self.replace_na(_new)
        }
    }

    fn replace_by_na(&self, old: T) {
        let n = self.size();
        let mut vec = self.values_mut();
        for i in 0..n {
            // TODO: Use get_unchecked_mut instead.
            // let ptr = unsafe { vec.get_unchecked_mut(i) };
            // if *ptr == old {
            //     *ptr = self.na_value();
            //     self.na_indexes_mut().insert(i);
            // }
            if vec[i] == old {
                vec[i] = self.na_value();
                self.na_indexes_mut().insert(i);
            }
        }
    }

    fn replace_elem(&self, old: T, new: T) {
        let n = self.size();
        let mut vec = self.values_mut();
        for i in 0..n {
            // TODO: Use get_unchecked_mut instead.
            // let ptr = unsafe { vec.get_unchecked_mut(i) };
            // if *ptr == old {
            //     *ptr = new.clone();
            // }
            if vec[i] == old {
                vec[i] = new.clone();
            }
        }
    }

    fn replace_na(&self, new: T) {
        let mut vec = self.values_mut();
        for i in self.na_indexes().iter() {
            // TODO: Use get_unchecked_mut instead.
            // let ptr = unsafe { vec.get_unchecked_mut(*i) };
            // *ptr = new.clone();
            vec[*i] = new.clone();
        }
        self.na_indexes_mut().clear();
    }

    fn set(&self, index: usize, elem: Option<T>) -> PyResult<()> {
        if index >= self.size() {
            return Err(PyIndexError::new_err("Index out of range!"));
        }
        let mut vec = self.values_mut();
        // TODO: Use get_unchecked_mut instead.
        // let ptr = unsafe { vec.get_unchecked_mut(index) };
        // if let Some(i) = elem {
        //     *ptr = i;
        // } else {
        //     *ptr = self.na_value();
        //     self.na_indexes_mut().insert(index);
        // }
        if let Some(i) = elem {
            vec[index] = i;
            self.na_indexes_mut().remove(&index);
        } else {
            vec[index] = self.na_value();
            self.na_indexes_mut().insert(index);
        }
        Ok(())
    }

    fn repeat(elem: T, size: usize) -> Self {
        let vec = vec![elem; size];
        let hset = HashSet::new();
        List::_new(vec, hset)
    }

    fn size(&self) -> usize {
        self.values().len()
    }

    fn to_list(&self) -> Vec<Option<T>> {
        let mut vec: Vec<Option<T>> = self.values().iter().map(|x| Some(x.clone())).collect();
        for i in self.na_indexes().iter() {
            // let ptr = unsafe { vec.get_unchecked_mut(*i) };
            // *ptr = None;
            vec[*i] = None;
        }
        vec
    }

    fn union_all(&self, other: &Self) -> Self {
        let vec = self
            .values()
            .iter()
            .cloned()
            .chain(other.values().iter().cloned())
            .collect();
        let mut hset = self.na_indexes().clone();
        for i in other.na_indexes().iter() {
            hset.insert(i + self.size());
        }
        List::_new(vec, hset)
    }

    fn values(&self) -> Ref<Vec<T>>;

    fn values_mut(&self) -> RefMut<Vec<T>>;
}
