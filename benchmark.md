### How do we benchmark?
This benchmarking task is run by Github actions on ubuntu-latest. This document would be updated every time a new version is released.  

For each dtype like `int`, `float`, `str` and `bool`, there would be some sub-tasks to compare the performances between `ulist` and `numpy`. There are 5 rounds for each sub-task with different array sizes and number of runs:
* XS - array size 100, run 100K times;
* S - array size 1K, run 100K times;
* M - array size 10K, run 10K times;
* L - array size 100K, run 1K times;
* XL - array size 1M, run 100 times.

and the result of each round and the average result are both recorded.

### What does the result mean?
The benchmark score would be displayed as a markdown table similar to below:

| Item     | Dtype | XS   | S    | M    | L    | XL   | Average |
| -------- | ----- | ---- | ---- | ---- | ---- | ---- | ------- |
| AddOne   | int   | 0.9x | 1.0x | 1.0x | 1.0x | 1.1x | 1.0x    |
| ArraySum | int   | 4.8x | 6.2x | 7.4x | 6.4x | 7.3x | 6.4x    |
| EqualOne | int   | 1.3x | 1.3x | 1.0x | 0.9x | 0.8x | 1.1x    |

Item - The task to compare the performances.
Dtype - The array element type.

Take the 3rd line for example, it means by running the task `EqualOne` with
`dtype=int`, the `ulist`'s speed is 1.1 times of `numpy` on average.


### Benchmark score
Info:  
************************************************************
Date: 2022-02-26 10:38:31   
System OS: Linux   
CPU:  Intel(R) Xeon(R) CPU E5-2673 v3 @ 2.40GHz   
Python version: 3.10.2   
Ulist version: 0.8.0   
Numpy version: 1.22.0   
************************************************************

Result:

| Item         | Dtype  | XS    | S     | M     | L     | XL    | Average | Faster |
| ------------ | ------ | ----- | ----- | ----- | ----- | ----- | ------- | ------ |
| AddOne       | int    | 0.9x  | 1.0x  | 1.0x  | 1.0x  | 1.1x  | 1.0x    | N      |
| ArraySum     | int    | 6.0x  | 7.0x  | 8.4x  | 5.5x  | 7.0x  | 6.8x    | Y      |
| CountElems   | int    | 9.7x  | 1.7x  | 0.9x  | 0.8x  | 0.9x  | 2.8x    | Y      |
| EqualOne     | int    | 1.4x  | 1.4x  | 1.4x  | 0.9x  | 0.8x  | 1.2x    | Y      |
| Max          | int    | 4.4x  | 3.7x  | 3.2x  | 3.0x  | 3.2x  | 3.5x    | Y      |
| MulTwo       | int    | 1.0x  | 1.0x  | 0.8x  | 0.8x  | 0.8x  | 0.9x    | N      |
| UniqueElem   | int    | 2.7x  | 0.5x  | 0.4x  | 0.3x  | 0.3x  | 0.8x    | N      |
| Sort         | int    | 0.8x  | 0.6x  | 0.9x  | 0.9x  | 0.9x  | 0.8x    | N      |
| AddOne       | float  | 1.0x  | 1.2x  | 1.2x  | 1.1x  | 1.1x  | 1.1x    | Y      |
| ArraySum     | float  | 4.0x  | 2.0x  | 0.7x  | 0.4x  | 0.4x  | 1.5x    | Y      |
| LessThanOne  | float  | 1.2x  | 1.2x  | 0.9x  | 0.8x  | 1.0x  | 1.0x    | N      |
| Max          | float  | 2.9x  | 1.1x  | 0.2x  | 0.1x  | 0.1x  | 0.9x    | N      |
| MulTwo       | float  | 1.0x  | 1.0x  | 1.1x  | 1.0x  | 1.0x  | 1.0x    | N      |
| Sort         | float  | 0.9x  | 0.6x  | 0.7x  | 0.7x  | 0.7x  | 0.7x    | N      |
| AllIsTrue    | bool   | 5.5x  | 3.4x  | 1.2x  | 0.7x  | 0.6x  | 2.3x    | Y      |
| AndOp        | bool   | 0.5x  | 0.8x  | 1.3x  | 4.3x  | 3.8x  | 2.1x    | Y      |
| AnyIsTrue    | bool   | 5.4x  | 3.4x  | 1.2x  | 0.7x  | 0.6x  | 2.3x    | Y      |
| NotOp        | bool   | 0.6x  | 0.9x  | 1.5x  | 4.9x  | 4.5x  | 2.5x    | Y      |
| OrOp         | bool   | 0.5x  | 0.8x  | 1.4x  | 3.6x  | 3.4x  | 1.9x    | Y      |
| ContainsElem | string | 16.4x | 20.1x | 20.6x | 20.7x | 20.3x | 19.6x   | Y      |
| CountElems   | string | 4.7x  | 1.7x  | 1.5x  | 1.9x  | 2.1x  | 2.4x    | Y      |
| EqualFoo     | string | 1.2x  | 2.8x  | 3.6x  | 3.9x  | 2.5x  | 2.8x    | Y      |

14 of 22 tasks are faster!