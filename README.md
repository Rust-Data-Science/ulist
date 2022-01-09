# ulist

[![PyPI](https://img.shields.io/pypi/v/ulist)](https://pypi.org/project/ulist/)
![PyPI - Format](https://img.shields.io/pypi/format/ulist)
[![License](https://img.shields.io/github/license/tushushu/ulist)](https://github.com/tushushu/ulist/blob/main/LICENSE)
[![CI](https://github.com/tushushu/ulist/workflows/CI/badge.svg)](https://github.com/tushushu/ulist/actions/workflows/main.yml)
[![doc](https://github.com/tushushu/ulist/workflows/doc/badge.svg)](https://github.com/tushushu/ulist/actions/workflows/sphinx.yml)
[![publish](https://github.com/tushushu/ulist/workflows/publish/badge.svg)](https://github.com/tushushu/ulist/actions/workflows/publish.yml)
[![Code Style](https://img.shields.io/badge/code%20style-flake8-blue)](https://github.com/PyCQA/flake8)  
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/tushushu/3a76a8f4c0d25c24b840fe66a3cf44c1/raw/dde38d61670379e703400ea2d89d88c5a3bb2588/metacov.json)](https://github.com/tushushu/ulist/actions/workflows/coverage.yml)  
  
    
[**Documentation**](https://tushushu.github.io/ulist/) | [**Source Code**](https://github.com/tushushu/ulist)  


### What
Ulist is an ultra fast list data structures written in Rust with Python bindings.


### Requirements
* Python: 3.7+    
* OS: Linux or MacOS


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
* `ge` and `le` methods for `FloatList`
* `apply`, `where`, `nth`, `argmin`, `argmax`, `median`, `top` methods for `NumericalList`
* Implement `StringList` or `BytesList`
* `var` method for `IntegerList` and `BooleanList`
* `union` and `case-when` methods for `List` class
* Implement `IndexList`
* Remove unnecessary methods for `BooleanList`, and user can cast `BooleanList` to `IntegerList` if needed.
* Support Windows users
* Code coverage test
* Doctest to check examples in Docstrings
* Inplace and non-inplace mode
* Support missing values
* Airspeed velocity to benchmark
* Further optimizing the benchmark with SIMD

### Contribute
All contributions are welcome. See [Developer Guide](https://github.com/tushushu/ulist/blob/main/develop.md)
