# ulist
Ultra fast list data structures written in Rust with Python bindings.


### Install
Run `pip install ulist`


### Compatibility
Python: 3.6+  
OS: Linux or MacOS


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


### Develop
`ulist` is built and published by `maturin`, so make sure you have `maturin` installed before developing anything.


### Build
* Run `maturin develop` to build the crate and install it as a python module directly in the current virtualenv. Note that while maturin develop is faster, it doesn't support all the features that running pip install after `maturin build` supports.
* Run `maturin build` to build the wheels and store them in a folder (target/wheels by default), but doesn't upload them. It's possible to upload those with twine.
* Run `maturin build --release` If we want to benchmark the package.


### Publish
`maturin publish` builds the crate into python packages and publishes them to pypi.


### Docker
The docker images are saved in https://hub.docker.com/repository/docker/tushushu/ulist
* Build by docker, please run `docker run -it -i <image ID>`, and then run `maturin build`.
* Customize the build, please consider to change the arguments `gh_username`, 
`ulist_home` and `branch` in the `Dockerfile` before building.
* run `docker cp <containerId>:/home/ulist/ulist/target/wheels /host/path/target` to copy the wheel for Linux to local disk.


### Wish-list
* `sum`, `any`, and `all` methods for `BooleanList`
* `map`, `where` methods for `NumericalList`
* `zip` method for `List` and `ListPair` class
* `agg` method for `ListPair`
* More construction methods for `List`
* Logical operators for `BooleanList`
* Comparison operators `NumericalList`
* Airspeed velocity to benchmark
* Automatically generate documentation
* More boundary check logics
* Mypy linting
* Stub files
