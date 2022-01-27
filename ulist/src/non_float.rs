use crate::base::List;
use std::collections::HashMap;
use std::hash::Hash;

pub trait NonFloatList<T>: List<T>
where
    T: Ord + Hash + Sized + Clone,
{
    // Arrange the following methods in alphabetical order.
    fn _sort(&self, vec: &mut Vec<T>, ascending: bool) {
        if ascending {
            vec.sort();
        } else {
            vec.sort_by(|a, b| b.cmp(a))
        }
    }

    fn counter(&self) -> HashMap<T, usize> {
        let vec = self.values();
        let mut result: HashMap<T, usize> = HashMap::new();
        for key in vec.iter() {
            let val = result.entry(key.clone()).or_insert(0);
            *val += 1;
        }
        result
    }

    fn sort(&self, ascending: bool) -> Self {
        let mut vec = self.to_list();
        let mut _vec = &mut vec;
        self._sort(_vec, ascending);
        List::_new(vec)
    }

    fn unique(&self) -> Self {
        let mut vec = self.to_list();
        self._sort(&mut vec, true);
        vec.dedup();
        List::_new(vec)
    }
}
