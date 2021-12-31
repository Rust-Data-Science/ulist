# ulist

![PyPI](https://img.shields.io/pypi/v/ulist)
![License](https://img.shields.io/github/license/tushushu/ulist)
![CI](https://github.com/tushushu/ulist/workflows/CI/badge.svg)
![PyPI - Format](https://img.shields.io/pypi/format/ulist)
![Code Style](https://img.shields.io/badge/code%20style-flake8-blue)  
  
    
[**Documentation**](https://tushushu.github.io/ulist/) | [**Source Code**](https://github.com/tushushu/ulist)  


### What
Ulist is an ultra fast list data structures written in Rust with Python bindings.


### Requirements
Python: 3.6+  
OS: Linux or MacOS


### Installation
Run `pip install ulist`


### Examples

#### Calculate the average of unique numbers.
```Python
import ulist as ul

arr = ul.from_iter([1.0, 2.0, 3.0, 2.0, 4.0, 5.0], dtype="float")
result = arr.unique().mean()
print(result)
```


#### Dot product.
```Python
import ulist as ul

arr1 = ul.from_iter(range(1, 4), dtype="int")
arr2 = ul.from_iter(range(1, 4), dtype="int")
result = arr1.mul(arr2).sum()
print(result)
```


#### Subtract the mean from the list.
```Python
import ulist as ul

arr = ul.from_iter([1, 2, 3, 4, 5], dtype="float")
result = arr.sub_scala(arr.mean()).to_list()
print(result)
```


#### Use operators instead of methods to calculate variance.
```Python
import ulist as ul

arr = ul.from_iter([1, 2, 3], dtype="float")
result = ((arr - arr.mean()) ** 2).mean()
print(result)
```


### Wish-list
* `sum` method for `BooleanList`
* `map`, `where` methods for `NumericalList`
* `zip` method for `List` and `ListPair` class
* `agg` method for `ListPair`
* `StringList` or `BytesList` class
* More construction methods for `List`
* Airspeed velocity to benchmark
* Docstrings for python methods
* Automatically generate documentation
* Mypy linting
* Further optimizing the benchmark with SIMD

### Contribute
All contributions are welcome. See [Developer Guide](https://github.com/tushushu/ulist/blob/main/develop.md)
