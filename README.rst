ulist
=====

|PyPI| |License| |CI| |doc| |publish| |code style| |Coverage| |downloads/month|

`Documentation <https://rust-data-science.github.io/ulist/>`__ \| `Source
Code <https://github.com/tushushu/ulist>`__

What
~~~~

| Ulist is an ultra fast list/array data structure written in Rust with
  Python bindings. It aims to be the fundamental package for processing
  and computing 1-D list/array in Python.
| It provides:

-  an efficient, flexible and expressive 1-D list/array object;
-  broadcasting methods;
-  a SQL-like and method-chaining programming experience;

Performance
~~~~~~~~~~~

| Ulist is extremly fast, and even compared with libraries like Numpy.
  It is

- more efficient on the ``string`` and ``boolean`` array,
- same level efficient on the ``integer`` array,
- and a bit slower on the ``floating`` array.

Faster than Numpy is not the target of writing this repo, because they are just two different libraries. Ulist is more focused on general domain rather than just data science/machine learning/AI, for example the Linear Algebra Computation is not provided. But if you are curious about the performance, please see the `benchmarking results <https://github.com/tushushu/ulist/blob/main/benchmark.rst>`__.

Requirements
~~~~~~~~~~~~

-  Python: 3.7+
-  OS: Linux, MacOS and Windows

Installation
~~~~~~~~~~~~

Run ``pip install ulist``

Examples
~~~~~~~~

Count the number of items in bins.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given an array ``arr``, count the number of items in bins [0, 3), [3, 6), [6, 9) and [9, +inf). The ``result`` is a Python dictionary with bin names as keys and numbers as values.

.. code:: python

   >>> import ulist as ul

   >>> arr = ul.arange(12)
   >>> arr
   UltraFastList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

   >>> result = arr.case(default='[9, +inf)')\
   ...             .when(lambda x: x < 3, then='[0, 3)')\
   ...             .when(lambda x: x < 6, then='[3, 6)')\
   ...             .when(lambda x: x < 9, then='[6, 9)')\
   ...             .end()\
   ...             .counter()
   >>> result
   {'[3, 6)': 3, '[9, +inf)': 3, '[6, 9)': 3, '[0, 3)': 3}

Dot product.
^^^^^^^^^^^^

Given two 1-D arrays and calculate the dot product result of those arrays.

.. code:: python

   >>> import ulist as ul

   >>> arr = ul.from_seq(range(1, 4), dtype='float')
   >>> arr
   UltraFastList([1.0, 2.0, 3.0])

   >>> result = arr.mul(arr).sum()
   >>> result
   14.0

Rate of adults.
^^^^^^^^^^^^^^^

Given the ages of people as ``arr``, and suppose the adults are equal or above 18. Clean the data by removing abnormal values and then calculate the rate of adults.

.. code:: python

   >>> import ulist as ul

   >>> arr = ul.from_seq([-1, 10, 15, 20, 30, 50, 70, 80, 100, 200], dtype='int')
   >>> result = arr.where(lambda x: (x >= 0) & (x < 120))\
   ...             .apply(lambda x: x >= 18)\
   ...             .mean()
   >>> result
   0.75

Contribute
~~~~~~~~~~

All contributions are welcome. See `Developer Guide <https://github.com/tushushu/ulist/blob/main/develop.rst>`__

.. |PyPI| image:: https://badge.fury.io/py/ulist.svg
   :target: https://pypi.org/project/ulist/
.. |License| image:: https://img.shields.io/github/license/tushushu/ulist
   :target: https://github.com/tushushu/ulist/blob/main/LICENSE
.. |CI| image:: https://github.com/tushushu/ulist/actions/workflows/main.yml/badge.svg
   :target: https://github.com/tushushu/ulist/actions/workflows/main.yml
.. |doc| image:: https://github.com/tushushu/ulist/actions/workflows/sphinx.yml/badge.svg
   :target: https://github.com/tushushu/ulist/actions/workflows/sphinx.yml
.. |publish| image:: https://github.com/tushushu/ulist/actions/workflows/publish.yml/badge.svg?branch=0.11.0
   :target: https://github.com/tushushu/ulist/actions/workflows/publish.yml
.. |code style| image:: https://img.shields.io/badge/style-flake8-blue
   :target: https://github.com/PyCQA/flake8
.. |Coverage| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/tushushu/3a76a8f4c0d25c24b840fe66a3cf44c1/raw/metacov.json
   :target: https://github.com/tushushu/ulist/actions/workflows/coverage.yml
.. |downloads/month| image:: https://static.pepy.tech/badge/ulist/month
   :target: https://pypi.org/project/ulist/
