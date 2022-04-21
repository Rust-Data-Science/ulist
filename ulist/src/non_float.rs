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
        result[&self.na_value()] -= self.count_na();
        if result[&self.na_value()] == 0 {
            result.remove(&self.na_value());
        }
        result
    }

    unsafe fn sort(&self, ascending: bool) {
        if self.count_na() == self.size() {
            return;
        }
        let vec = self.values_mut();
        let hset = self.na_indexes();
        // Put all the na elements to the right side.
        let mut l = 0;
        let mut r = self.size() - 1;
        while l < r && !hset.is_empty() {
            while l < r && !hset.contains(&l) {
                l += 1;
            }
            while l < r && hset.contains(&r) {
                r -= 1;
            }
            let elem1 = vec.get_unchecked_mut(l);
            let elem2 = vec.get_unchecked_mut(r);
            *elem1 = *elem2;
            *elem2 = self.na_value();
        }
        // Update na indexes.
        hset.clear();
        for i in (self.size() - self.count_na())..self.size() {
            hset.insert(i);
        }
        // Sort non-na elements.
        let s = &mut vec[0..(self.size() - self.count_na())];
        if ascending {
            s.sort_unstable();
        } else {
            s.sort_unstable_by(|a, b| b.cmp(a))
        }
    }

    unsafe fn unique(&self) -> Self {
        // Get the unique values.
        let dedup = HashSet::with_capacity(self.size());
        for (i, &val) in self.values().iter().enumerate() {
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
        let vec = Vec::with_capacity(l);
        vec.set_len(l);
        for (i, &val) in dedup.iter().enumerate() {
            let elem = vec.get_unchecked_mut(i);
            *elem = val;
        }
        if self.count_na() > 0 {
            vec.push(self.na_value());
        }
        // Construct List.
        let hset = HashSet::new();
        hset.insert(vec.len() - 1);
        List::_new(vec, hset)
    }
}
