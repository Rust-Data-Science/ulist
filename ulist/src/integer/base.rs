pub trait IntegerList<T, U, V>: NumericalList<T, U>
where
    T: Copy + PartialOrd + Add<Output = T> + Sub<Output = T> + Mul<Output = T> + Div<Output = T>,
{
    // Arrange the following methods in alphabetical order.
    fn argmax(&self) -> usize {
        self.values()
            .iter()
            .enumerate()
            .max_by_key(|x| x.1)
            .unwrap()
            .0
    }

    fn argmin(&self) -> usize {
        self.values()
            .iter()
            .enumerate()
            .min_by_key(|x| x.1)
            .unwrap()
            .0
    }

    fn div(&self, other: &Self) -> Vec<f32> {
        self.values()
            .iter()
            .zip(other.values().iter())
            .map(|(&x, &y)| x as f32 / y as f32)
            .collect()
    }

    fn div_scala(&self, elem: f32) -> Vec<f32> {
        self.values().iter().map(|x| *x as f32 / elem).collect()
    }

    fn max(&self) -> i64 {
        *self.values().iter().max().unwrap()
    }

    fn min(&self) -> i64 {
        *self.values().iter().min().unwrap()
    }

    fn pow_scala(&self, elem: u32) -> Self {
        let vec = self.values().iter().map(|&x| x.pow(elem)).collect();
        IntegerList64::new(vec)
    }

    fn sum(&self) -> i64 {
        self.values().iter().sum()
    }
}
