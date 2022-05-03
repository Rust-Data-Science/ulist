use crate::boolean::BooleanList;
use crate::index::IndexList;
use std::cell::Ref;
use std::cell::RefMut;
use std::collections::HashSet;
use std::iter::FromIterator;

pub fn _fill_na<T: Clone>(vec: &mut Vec<T>, na_indexes: Ref<HashSet<usize>>, na_value: T) {
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

    fn _fn_scala<U>(&self, func: impl Fn(&T) -> U) -> Vec<U> {
        self.values().iter().map(|x| func(x)).collect()
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
        }
        // Update na indexes.
        hset.clear();
        for i in (n - m)..n {
            hset.insert(i);
        }
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

    fn cycle(vec: &Vec<T>, size: usize) -> Self {
        let v = vec.iter().cycle().take(size).map(|x| x.clone()).collect();
        List::_new(v, HashSet::new())
    }

    fn equal_scala(&self, elem: T) -> BooleanList {
        let mut vec = self._fn_scala(|x| x == &elem);
        _fill_na(&mut vec, self.na_indexes(), false);
        BooleanList::new(vec, HashSet::new())
    }

    fn filter(&self, condition: &BooleanList) -> Self {
        let vec = self
            .values()
            .iter()
            .zip(condition.values().iter())
            .filter(|(_, y)| **y)
            .map(|(x, _)| x.clone())
            .collect();
        // TODO: Report bug of below codes.
        let cond = condition.values();
        let hset = self
            .na_indexes()
            .iter()
            .filter(|&x| cond[*x])
            .map(|x| x.clone())
            .collect();
        List::_new(vec, hset)
    }

    fn get(&self, index: usize) -> Option<T> {
        if self.na_indexes().contains(&index) {
            return None;
        }
        let vec = self.values();
        let val = vec.get(index);
        if let Some(i) = val {
            return Some(i.clone());
        } else {
            panic!("Index out of range!")
        }
    }

    fn get_by_indexes(&self, indexes: &IndexList) -> Self {
        if indexes.back() >= self.size() {
            panic!("Index out of range!")
        }
        let vec = unsafe {
            indexes
                .values()
                .iter()
                .map(|&x| self.values().get_unchecked(x).clone())
                .collect()
        };
        let mut hset = HashSet::with_capacity(self.size());
        for i in indexes.values().iter() {
            if self.na_indexes().contains(i) {
                hset.insert(i.clone());
            }
        }
        hset.shrink_to_fit();
        List::_new(vec, hset)
    }

    fn has_na(&self) -> bool {
        self.count_na() > 0
    }

    fn na_indexes(&self) -> Ref<HashSet<usize>>;

    fn na_indexes_mut(&self) -> RefMut<HashSet<usize>>;

    fn na_value(&self) -> T;

    fn not_equal_scala(&self, elem: T) -> BooleanList {
        let mut vec = self._fn_scala(|x| x != &elem);
        _fill_na(&mut vec, self.na_indexes(), false);
        BooleanList::new(vec, HashSet::new())
    }

    fn pop(&self) {
        let i = self.size() - 1;
        if self.na_indexes().contains(&i) {
            self.na_indexes_mut().remove(&i);
        }
        self.values_mut().pop();
    }

    fn replace(&self, old: Option<T>, new: Option<T>) {
        if let Some(_old) = old {
            if let Some(_new) = new {
                self.replace_elem(_old, _new)
            } else {
                self.replace_by_na(_old)
            }
        } else {
            if let Some(_new) = new {
                self.replace_na(_new)
            }
        }
    }

    fn replace_by_na(&self, old: T) {
        let n = self.size();
        let mut vec = self.values_mut();
        for i in 0..n {
            let ptr = unsafe { vec.get_unchecked_mut(i) };
            if *ptr == old {
                *ptr = self.na_value();
                self.na_indexes_mut().insert(i);
            }
        }
    }

    fn replace_elem(&self, old: T, new: T) {
        let n = self.size();
        let mut vec = self.values_mut();
        for i in 0..n {
            let ptr = unsafe { vec.get_unchecked_mut(i) };
            if *ptr == old {
                *ptr = new.clone();
            }
        }
    }

    fn replace_na(&self, new: T) {
        let mut vec = self.values_mut();
        for i in self.na_indexes().iter() {
            let ptr = unsafe { vec.get_unchecked_mut(*i) };
            *ptr = new.clone();
        }
        self.na_indexes_mut().clear();
    }

    fn set(&self, index: usize, elem: Option<T>) {
        if index >= self.size() {
            panic!("Index out of range!")
        }
        let mut values = self.values_mut();
        let ptr = unsafe { values.get_unchecked_mut(index) };
        if let Some(i) = elem {
            *ptr = i;
        } else {
            *ptr = self.na_value();
            self.na_indexes_mut().insert(index);
        }
    }

    fn repeat(elem: Option<T>, size: usize, na_value: T) -> Self {
        let mut val = na_value;
        let mut hset = HashSet::new();
        if let Some(i) = elem {
            val = i;
        } else {
            hset = HashSet::from_iter(0..size);
        }
        let vec = vec![val; size];
        List::_new(vec, hset)
    }

    fn size(&self) -> usize {
        self.values().len()
    }

    fn to_list(&self) -> Vec<Option<T>> {
        let mut vec: Vec<Option<T>> = self.values().iter().map(|x| Some(x.clone())).collect();
        for i in self.na_indexes().iter() {
            let ptr = unsafe { vec.get_unchecked_mut(*i) };
            *ptr = None;
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
