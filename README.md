# ulist
Ultra fast list - Python bindings to Rust Vector.   


### Install
`pip install ulist`  


### Develop
`ulist` is built and published by `maturin`, so make sure you have `maturin` installed before developing anything.


### Build
* Run `maturin develop` to build the crate and install it as a python module directly in the current virtualenv. Note that while maturin develop is faster, it doesn't support all the features that running pip install after `maturin build` supports.
* Run `maturin build` to build the wheels and store them in a folder (target/wheels by default), but doesn't upload them. It's possible to upload those with twine.
* Run `maturin build --release` If we want to benchmark the package.


### Build by docker
* Run `docker build .` to build the docker image.
* Run `docker cp <container>:"/home/ulist/ulist/target/release/wheels/" <local-dest-path> ` to copy the wheels folder and files from docker container to local path.


### Publish
`maturin publish` builds the crate into python packages and publishes them to pypi.
