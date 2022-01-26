use crate::boolean::BooleanList;
use std::cell::Ref;
use std::cell::RefMut;

/// Abstract List with generic type elements.
pub trait List<T>
where
    T: PartialEq + Clone,
    Self: Sized,
{
    // Arrange the following methods in alphabetical order.

    fn _new(vec: Vec<T>) -> Self;

    fn _operate_scala<U>(&self, func: impl Fn(T) -> U) -> Vec<U> {
        self.values().iter().map(|&x| func(x)).collect()
    }

    fn append(&self, elem: T) {
        self.values_mut().push(elem);
    }

    fn copy(&self) -> Self {
        List::_new(self.to_list())
    }

    fn cycle(vec: &Vec<T>, size: usize) -> Self {
        let v = vec.iter().cycle().take(size).map(|x| x.clone()).collect();
        List::_new(v)
    }

    fn equal_scala(&self, elem: T) -> BooleanList {
        BooleanList::new(self._operate_scala(|x| x == elem))
    }

    fn filter(&self, condition: &BooleanList) -> Self {
        let vec = self
            .values()
            .iter()
            .zip(condition.values().iter())
            .filter(|(_, y)| **y)
            .map(|(x, _)| *x)
            .collect();
        List::_new(vec)
    }

    unsafe fn get(&self, index: usize) -> T {
        if index < self.size() {
            self.values().get_unchecked(index).clone()
        } else {
            panic!("Index out of range!")
        }
    }

    fn not_equal_scala(&self, elem: T) -> BooleanList {
        BooleanList::new(self._operate_scala(|x| x != elem))
    }

    fn pop(&self) {
        self.values_mut().pop();
    }

    fn replace(&self, old: T, new: T) -> Self {
        let vec = self
            .values()
            .iter()
            .map(|&x| if x == old { new } else { x })
            .collect();
        List::_new(vec)
    }

    unsafe fn set(&self, index: usize, elem: T) {
        if index < self.size() {
            let mut values = self.values_mut();
            let element = values.get_unchecked_mut(index);
            *element = elem
        } else {
            panic!("Index out of range!")
        }
    }

    fn repeat(elem: T, size: usize) -> Self {
        let vec = vec![elem; size];
        List::_new(vec)
    }

    fn size(&self) -> usize {
        self.values().len()
    }

    fn to_list(&self) -> Vec<T> {
        self.values().clone()
    }

    fn union_all(&self, other: &Self) -> Self {
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
