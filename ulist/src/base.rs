use std::cell::Ref;
use std::cell::RefMut;
use std::clone::Clone;
use std::cmp::PartialEq;
use std::marker::Copy;
use std::marker::Sized;

/// Abstract List with generic type elements.
pub trait List<T>
where
    T: Clone + PartialEq + Copy,
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

    fn replace(&self, old: T, new: &T) {
        for element in self.values_mut().iter_mut() {
            if *element == old {
                *element = *new;
            }
        }
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

    fn values(&self) -> Ref<Vec<T>>;

    fn values_mut(&self) -> RefMut<Vec<T>>;
}
