How do we benchmark?
~~~~~~~~~~~~~~~~~~~~

This benchmarking task is run by Github actions on ubuntu-latest. This document would be updated every time a new version is released.

For each dtype like ``int``, ``float``, ``str`` and ``bool``, there would be some sub-tasks to compare the performances between ``ulist`` and ``numpy``. There are 5 rounds for each sub-task with different array sizes and number of runs:

- XS - array size 100, run 100K times;
- S - array size 1K, run 100K times;
- M - array size 10K, run 10K times;
- L - array size 100K, run 1K times;
- XL - array size 1M, run 100 times.

and the result of each round and the average result are both recorded.

What does the result mean?
~~~~~~~~~~~~~~~~~~~~~~~~~~

The benchmark score would be displayed as a markdown table similar to below:

======== ===== ==== ==== ==== ==== ==== =======
Item     Dtype XS   S    M    L    XL   Average
======== ===== ==== ==== ==== ==== ==== =======
AddOne   int   0.9x 1.0x 1.0x 1.0x 1.1x 1.0x
ArraySum int   4.8x 6.2x 7.4x 6.4x 7.3x 6.4x
EqualOne int   1.3x 1.3x 1.0x 0.9x 0.8x 1.1x
======== ===== ==== ==== ==== ==== ==== =======

Item - The task to compare the performances.
Dtype - The array element type.

Take the 3rd line for example, it means by running the task ``EqualOne`` with
``dtype=int``, the ``ulist``\ ’s speed is 1.1 times of ``numpy`` on average.

Benchmark score
~~~~~~~~~~~~~~~

| Info:

----

| Date: 2022-05-21 07:58:18
| System OS: Linux
| CPU:  Intel(R) Xeon(R) CPU E5-2673 v4 @ 2.30GHz
| Python version: 3.10.4
| Ulist version: 0.10.0
| Numpy version: 1.22.0

----

Result:

============ ====== ===== ===== ===== ===== ===== ======= ======
Item         Dtype  XS    S     M     L     XL    Average Faster
============ ====== ===== ===== ===== ===== ===== ======= ======
AddOne       int    0.9x  0.9x  0.6x  0.5x  0.5x  0.7x    N
ArraySum     int    4.1x  4.8x  4.7x  3.8x  3.8x  4.2x    Y
CountElems   int    7.1x  1.4x  0.9x  0.8x  0.9x  2.2x    Y
EqualOne     int    1.1x  0.9x  0.4x  0.4x  0.3x  0.6x    N
Max          int    2.3x  1.7x  1.0x  0.8x  0.9x  1.3x    Y
MulTwo       int    0.9x  0.9x  0.6x  0.5x  0.5x  0.7x    N
UniqueElem   int    2.2x  0.6x  1.0x  1.1x  1.1x  1.2x    Y
Sort         int    3.6x  18.2x 81.0x 107x  80.7x 58.1x   Y
AddOne       float  0.9x  0.9x  0.6x  0.5x  0.5x  0.7x    N
ArraySum     float  2.6x  1.4x  0.6x  0.4x  0.4x  1.1x    Y
LessThanOne  float  1.1x  0.9x  0.4x  0.3x  0.3x  0.6x    N
Max          float  1.4x  0.3x  0.1x  0.0x  0.0x  0.4x    N
MulTwo       float  0.9x  0.9x  0.7x  0.5x  0.5x  0.7x    N
Sort         float  3.0x  13.7x 32.1x 38.9x 29.6x 23.5x   Y
AllIsTrue    bool   3.5x  2.4x  1.0x  0.8x  0.6x  1.7x    Y
AndOp        bool   0.5x  0.7x  1.1x  3.2x  3.7x  1.8x    Y
AnyIsTrue    bool   3.6x  2.2x  1.0x  0.7x  0.6x  1.6x    Y
NotOp        bool   0.5x  0.7x  1.3x  4.6x  4.1x  2.2x    Y
OrOp         bool   0.5x  0.7x  1.3x  4.0x  3.6x  2.0x    Y
ContainsElem string 15.6x 19.3x 20.0x 20.0x 19.8x 18.9x   Y
CountElems   string 4.1x  1.5x  1.6x  1.9x  2.2x  2.3x    Y
EqualFoo     string 1.2x  2.8x  3.6x  3.9x  2.5x  2.8x    Y
============ ====== ===== ===== ===== ===== ===== ======= ======

15 of 22 tasks are faster!
