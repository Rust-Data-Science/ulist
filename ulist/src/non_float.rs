use crate::base::List;
use std::collections::HashMap;
use std::collections::HashSet;
use std::hash::Hash;

pub trait NonFloatList<T>: List<T>
where
    T: Ord + Hash + Sized + Clone,
{
    // Arrange the following methods in alphabetical order.
    fn counter(&self) -> HashMap<T, usize> {
        let vec = self.values();
        let mut result: HashMap<T, usize> = HashMap::new();
        for key in vec.iter() {
            let val = result.entry(key.clone()).or_insert(0);
            *val += 1;
        }
        // Exclude the count of na values.
        if let Some(val) = result.get_mut(&self.na_value()) {
            *val -= self.count_na();
            if *val == 0 {
                result.remove(&self.na_value());
            }
        }
        result
    }

    fn sort(&self, ascending: bool) {
        // Handle na elements.
        self._sort();
        // Sort non-na elements.
        let mut vec = self.values_mut();
        let s = &mut vec[0..(self.size() - self.count_na())];
        if ascending {
            s.sort_unstable();
        } else {
            s.sort_unstable_by(|a, b| b.cmp(a))
        }
    }

    fn unique(&self) -> Self {
        // Get the unique values.
        let mut dedup = HashSet::with_capacity(self.size());
        let vec = self.values();
        for (i, val) in vec.iter().enumerate() {
            if self.na_indexes().contains(&i) {
                continue;
            }
            dedup.insert(val);
        }
        // Copy the unique and na values to the vec.
        let mut l = dedup.len();
        if self.count_na() > 0 {
            l += 1;
        }
        let mut vec_dedup = Vec::with_capacity(l);
        unsafe { vec_dedup.set_len(l) };
        for (i, &val) in dedup.iter().enumerate() {
            let elem = unsafe { vec_dedup.get_unchecked_mut(i) };
            *elem = val.clone();
        }
        if self.count_na() > 0 {
            vec_dedup.push(self.na_value());
        }
        // Construct List.
        let mut hset = HashSet::new();
        if self.count_na() > 0 {
            hset.insert(vec_dedup.len() - 1);
        }
        List::_new(vec_dedup, hset)
    }
}
