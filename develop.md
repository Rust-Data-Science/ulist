# Develop 

### Packages
* `ulist` is built and published by `maturin`, so make sure you have `maturin` installed before developing anything;
* `pytest` is the testing framework for `ulist`, we aim to 100% test coverage;
* `Flake8` and `mypy` are the linters for `ulist`, they help us to check the code style, bugs and type annotation;
* `sphinx` auto-generates API documentation for `ulist`.


### Build
* Run `maturin develop` to build the crate and install it as a python module directly in the current virtualenv. Note that while maturin develop is faster, it doesn't support all the features that running pip install after `maturin build` supports.
* Run `maturin build` to build the wheels and store them in a folder (target/wheels by default), but doesn't upload them. It's possible to upload those with twine.
* Run `maturin build --release` If we want to benchmark the package.


### Docker
The docker images are saved in https://hub.docker.com/repository/docker/tushushu/ulist
* Build by docker, please run `docker run -it -i <image ID>`, and then run `maturin build`.
* Customize the build, please consider to change the arguments `gh_username`, 
`ulist_home` and `branch` in the `Dockerfile` before building.
* run `docker cp <containerId>:/home/ulist/ulist/target/wheels /host/path/target` to copy the wheel for Linux to local disk.
