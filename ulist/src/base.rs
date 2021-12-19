use std::cell::Ref;
use std::cell::RefMut;
use std::clone::Clone;
use std::marker::Sized;

/// Abstract List with generic type elements.
pub trait List<T>
where
    T: Clone,
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

    fn get(&self, index: usize) -> T {
        self.values()[index].clone()
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
