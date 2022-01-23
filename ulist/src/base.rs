use std::cell::Ref;
use std::cell::RefMut;
use std::cmp::Eq;
use std::cmp::PartialEq;
use std::collections::HashMap;
use std::hash::Hash;
use std::marker::Sized;

/// Abstract List with generic type elements.
pub trait List<T>
where
    T: PartialEq + Clone,
    Self: Sized,
{
    // Arrange the following methods in alphabetical order.

    fn _new(vec: Vec<T>) -> Self;

    fn append(&self, num: T) {
        self.values_mut().push(num);
    }

    fn copy(&self) -> Self {
        List::_new(self.to_list())
    }

    fn cycle(vec: &Vec<T>, size: usize) -> Self {
        let v = vec.iter().cycle().take(size).map(|x| x.clone()).collect();
        List::_new(v)
    }

    unsafe fn get(&self, index: usize) -> T {
        if index < self.size() {
            self.values().get_unchecked(index).clone()
        } else {
            panic!("Index out of range!")
        }
    }

    fn pop(&self) {
        self.values_mut().pop();
    }

    unsafe fn set(&self, index: usize, num: T) {
        if index < self.size() {
            let mut values = self.values_mut();
            let element = values.get_unchecked_mut(index);
            *element = num
        } else {
            panic!("Index out of range!")
        }
    }

    fn repeat(num: T, size: usize) -> Self {
        let vec = vec![num; size];
        List::_new(vec)
    }

    fn size(&self) -> usize {
        self.values().len()
    }

    fn to_list(&self) -> Vec<T> {
        self.values().clone()
    }

    fn union(&self, other: &Self) -> Self {
        let vec = self
            .values()
            .iter()
            .cloned()
            .chain(other.values().iter().cloned())
            .collect();
        List::_new(vec)
    }

    fn values(&self) -> Ref<Vec<T>>;

    fn values_mut(&self) -> RefMut<Vec<T>>;
}

// TODO: Move this method inside `List` trait.
pub fn counter<T: Eq + Hash + Copy>(vec: Ref<Vec<T>>) -> HashMap<T, usize> {
    let mut result: HashMap<T, usize> = HashMap::new();
    for key in vec.iter() {
        let val = result.entry(*key).or_insert(0);
        *val += 1;
    }
    result
}
