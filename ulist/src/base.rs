use std::clone::Clone;
use std::marker::Sized;

/// Abstract List with generic type elements.
pub trait List<'a, T>
where
    T: Clone,
    Self: Sized,
{
    // Arrange the following methods in alphabetical order.

    fn _new(vec: Vec<T>) -> Self;

    fn copy(&'a self) -> Self {
        List::_new(self.to_list())
    }

    fn size(&self) -> usize {
        self.values().len()
    }

    fn to_list(&self) -> Vec<T> {
        self.values().clone()
    }

    fn values(&self) -> &Vec<T>;
}
