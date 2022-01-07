# ulist

[![PyPI](https://img.shields.io/pypi/v/ulist)](https://pypi.org/project/ulist/)
![PyPI - Format](https://img.shields.io/pypi/format/ulist)
[![License](https://img.shields.io/github/license/tushushu/ulist)](https://github.com/tushushu/ulist/blob/main/LICENSE)
[![CI](https://github.com/tushushu/ulist/workflows/CI/badge.svg)](https://github.com/tushushu/ulist/actions/workflows/main.yml)
[![doc](https://github.com/tushushu/ulist/workflows/doc/badge.svg)](https://github.com/tushushu/ulist/actions/workflows/sphinx.yml)
[![publish](https://github.com/tushushu/ulist/workflows/publish/badge.svg)](https://github.com/tushushu/ulist/actions/workflows/publish.yml)
[![Code Style](https://img.shields.io/badge/code%20style-flake8-blue)](https://github.com/PyCQA/flake8)  
  
    
[**Documentation**](https://tushushu.github.io/ulist/) | [**Source Code**](https://github.com/tushushu/ulist)  


### What
Ulist is an ultra fast list data structures written in Rust with Python bindings.


### Requirements
Python: 3.7+  
OS: Linux or MacOS


### Installation
Run `pip install ulist`


### Examples

#### Calculate the average of unique numbers.
```Python
import ulist as ul

arr = ul.from_seq([1.0, 2.0, 3.0, 2.0, 4.0, 5.0], dtype="float")
result = arr.unique().mean()
print(result)
```


#### Dot product.
```Python
import ulist as ul

arr1 = ul.arange(1, 4)
arr2 = ul.arange(1, 4)
result = arr1.mul(arr2).sum()
print(result)
```


#### Subtract the mean from the list.
```Python
import ulist as ul

arr = ul.from_seq([1, 2, 3, 4, 5], dtype="float")
result = arr.sub_scala(arr.mean()).to_list()
print(result)
```


#### Use operators instead of methods to calculate variance.
```Python
import ulist as ul

arr = ul.from_seq([1, 2, 3], dtype="float")
result = ((arr - arr.mean()) ** 2).mean()
print(result)
```


### Wish-list
* `eq`, `ge`, `le` and `ne` methods for `FloatList`
* `map`, `where` methods for `NumericalList`
* `zip` method for `List` and `ListPair` class
* `agg` method for `ListPair`
* `StringList` or `BytesList` class
* `var` method for `IntegerList` and `BooleanList`
* Support Windows users
* Code coverage test
* Doctest to check examples in Docstrings
* Inplace and non-inplace mode
* Support missing values
* Airspeed velocity to benchmark
* Further optimizing the benchmark with SIMD

### Contribute
All contributions are welcome. See [Developer Guide](https://github.com/tushushu/ulist/blob/main/develop.md)
