# ulist
Ultra fast list - Python bindings to Rust Vector.


### Maturin
Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries as python packages.  
* `maturin publish` builds the crate into python packages and publishes them to pypi.
* `maturin build` builds the wheels and stores them in a folder (target/wheels by default), but doesn't upload them. It's possible to upload those with twine.
* `maturin develop` builds the crate and installs it as a python module directly in the current virtualenv. Note that while maturin develop is faster, it doesn't support all the feature that running pip install after `maturin build` supports.
* `marturin build --release` If we want to benchmark the package.
