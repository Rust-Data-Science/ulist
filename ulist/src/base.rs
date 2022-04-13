use crate::boolean::BooleanList;
use crate::index::IndexList;
use std::cell::Ref;
use std::cell::RefMut;
use std::collections::HashSet;
use std::iter::FromIterator;

/// Abstract List with generic type elements.
pub trait List<T>
where
    T: PartialEq + Clone,
    Self: Sized,
{
    // Arrange the following methods in alphabetical order.

    fn _new(vec: Vec<T>, hset: HashSet<usize>) -> Self;

    unsafe fn _fill_false(&self, vec: &Vec<bool>) {
        for i in self.na_indexes().iter() {
            let elem = vec.get_unchecked_mut(*i);
            *elem = false;
        }
    }

    fn _fn_scala<U>(&self, func: impl Fn(&T) -> U) -> Vec<U> {
        self.values().iter().map(|x| func(x)).collect()
    }

    fn append(&self, elem: Option<T>) {
        if let Some(i) = elem {
            self.values_mut().push(i);
        } else {
            self.na_indexes().insert(self.size());
            self.values_mut().push(self.na_value());
        }
    }

    fn copy(&self) -> Self {
        List::_new(self.values().clone(), self.na_indexes().clone())
    }

    fn count_na(&self) -> usize {
        self.na_indexes().len()
    }

    fn cycle(vec: &Vec<T>, size: usize) -> Self {
        let v = vec.iter().cycle().take(size).map(|x| x.clone()).collect();
        List::_new(v, HashSet::new())
    }

    unsafe fn equal_scala(&self, elem: T) -> BooleanList {
        let vec = self._fn_scala(|x| x == &elem);
        self._fill_false(&vec);
        BooleanList::new(vec, HashSet::new())
    }

    unsafe fn fill_na(&self, new: T) {
        for i in self.na_indexes().iter() {
            let elem = self.values_mut().get_unchecked_mut(*i);
            *elem = new;
        }
        self.na_indexes_mut().clear();
    }

    unsafe fn filter(&self, condition: &BooleanList) -> Self {
        let vec = self
            .values()
            .iter()
            .zip(condition.values().iter())
            .filter(|(_, y)| **y)
            .map(|(x, _)| x.clone())
            .collect();
        let hset = HashSet::new();
        for i in self.na_indexes().iter() {
            let cond = condition.values().get_unchecked(*i);
            if *cond {
                hset.insert(i.clone());
            }
        }
        List::_new(vec, hset)
    }

    fn get(&self, index: usize) -> Option<T> {
        if self.na_indexes().contains(&index) {
            return None;
        }
        let vec = self.values();
        let val = vec.get(index);
        if let Some(i) = val {
            return Some(*i);
        } else {
            panic!("Index out of range!")
        }
    }

    unsafe fn get_by_indexes(&self, indexes: &IndexList) -> Self {
        if indexes.back() >= self.size() {
            panic!("Index out of range!")
        }
        let vec = indexes
            .values()
            .iter()
            .map(|&x| self.values().get_unchecked(x).clone())
            .collect();
        let hset = HashSet::new();
        for i in indexes.values().iter() {
            if self.na_indexes().contains(i) {
                hset.insert(i.clone());
            }
        }
        List::_new(vec, hset)
    }

    fn has_na(&self) -> bool {
        self.count_na() > 0
    }

    fn na_indexes(&self) -> Ref<HashSet<usize>>;

    fn na_indexes_mut(&self) -> RefMut<HashSet<usize>>;

    fn na_value(&self) -> T;

    unsafe fn not_equal_scala(&self, elem: T) -> BooleanList {
        let vec = self._fn_scala(|x| x != &elem);
        self._fill_false(&vec);
        BooleanList::new(vec, HashSet::new())
    }

    fn pop(&self) {
        let i = self.size() - 1;
        if self.na_indexes().contains(&i) {
            self.na_indexes_mut().remove(&i);
        }
        self.values_mut().pop();
    }

    unsafe fn replace(&self, old: T, new: T) {
        for (i, x) in self.values().iter().enumerate() {
            if *x == old {
                let elem = self.values_mut().get_unchecked_mut(i);
                *elem = new
            }
        }
    }

    unsafe fn replace_by_na(&self, old: T) {
        for (i, x) in self.values().iter().enumerate() {
            if *x == old {
                let elem = self.values_mut().get_unchecked_mut(i);
                *elem = self.na_value();
                self.na_indexes_mut().insert(i);
            }
        }
    }

    unsafe fn set(&self, index: usize, elem: Option<T>) {
        if index >= self.size() {
            panic!("Index out of range!")
        }
        let mut values = self.values_mut();
        let element = values.get_unchecked_mut(index);
        if let Some(i) = elem {
            *element = i;
        } else {
            *element = self.na_value();
            self.na_indexes_mut().insert(index);
        }
    }

    fn repeat(&self, elem: Option<T>, size: usize) -> Self {
        let val = self.na_value();
        let hset = HashSet::new();
        if let Some(i) = elem {
            val = i;
        } else {
            hset = HashSet::from_iter(0..self.size());
        }
        let vec = vec![val; size];
        List::_new(vec, hset)
    }

    fn size(&self) -> usize {
        self.values().len()
    }

    unsafe fn to_list(&self) -> Vec<Option<T>> {
        let vec: Vec<Option<T>> = self.values().iter().map(|x| Some(x.clone())).collect();
        for i in self.na_indexes().iter() {
            let elem = vec.get_unchecked_mut(*i);
            *elem = None;
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
        let hset = self.na_indexes().clone();
        for i in other.na_indexes().iter() {
            hset.insert(i + self.size());
        }
        List::_new(vec, hset)
    }

    fn values(&self) -> Ref<Vec<T>>;

    fn values_mut(&self) -> RefMut<Vec<T>>;
}
