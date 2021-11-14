# ulist
Ultra fast list - Python bindings to Rust Vector.  


### Install
`pip install ulist`  


### Build and publish
`ulist` is built and published by `maturin`. The useful commands are listed as below:    
* `maturin develop` builds the crate and installs it as a python module directly in the current virtualenv. Note that while maturin develop is faster, it doesn't support all the features that running pip install after `maturin build` supports.
* `maturin build` builds the wheels and stores them in a folder (target/wheels by default), but doesn't upload them. It's possible to upload those with twine.
* `maturin build --release` If we want to benchmark the package.
* `maturin publish` builds the crate into python packages and publishes them to pypi.
