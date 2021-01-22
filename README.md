[![PyPI
version](https://badge.fury.io/py/truefalsepython.svg)](https://pypi.org/project/truefalsepython/)
[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://github.com/PasaOpasen/true-false-python/issues) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/PasaOpasen/true-false-python/pulls)

[![Downloads](https://pepy.tech/badge/truefalsepython)](https://pepy.tech/project/truefalsepython)
[![Downloads](https://pepy.tech/badge/truefalsepython/month)](https://pepy.tech/project/truefalsepython)
[![Downloads](https://pepy.tech/badge/truefalsepython/week)](https://pepy.tech/project/truefalsepython)

# true-false-python

PyPI package with some better syntax tools for python

```
pip install truefalsepython
```

- [true-false-python](#true-false-python)
  - [Logical tools](#logical-tools)
  - [Little functions](#little-functions)
  - [Useful functions](#useful-functions)
  - [R-like functions](#r-like-functions)

## Logical tools

For `True` and `False` values there are equal constants (like it is in C-like languages or R) `TRUE, T, true` and `FALSE, F, false`; for `None` there is `NULL` constant:

```python
from truefalsepython import TRUE, FALSE, T, F, true, false, NULL

print(True == T) # True
print(True == TRUE) # True
print(True == true) # True


print(False == F) # True
print(False == FALSE) # True
print(False == false) # True

print(NULL) # None
```

## Little functions

* `is_odd(number)`
* `is_even(number)`
* `is_number(object)`

## Useful functions

* `fast_sample(objects, probs)` -- returns 1 random object from `objects` with `probs` probabilities. It's faster than `np.random.choice(objects, 1, probs)` ([example](tests/fast_sample.py))
* `randomTrue(prob = 0.5)` -- returns `True` with probability `prob`, otherwise `False`


## R-like functions

For arrays there are several R-like functions:
* `nrow` — returns number of rows
* `ncol` — returns number of columns
* `colMeans` — returns average for each column
* `rowMeans` — returns average for each row
* `colSums` — returns sums for each column
* `rowSums` — returns sums for each row
* `apply` — applies function `FUN` to dimension of `arr2D` array (for rows if `MARGIN == 1` and columns if `MARGIN == 2`) 
* `lapply` — applies function `func` for each element in `array` (array/list or something else)
* `sapply` — like `lapply` but returns numpy array
* `sample` — it is `np.random.choice` but `replace = False` by default
* `sample_int` — sample numbers from `0` to `n-1`

Example of usage:

```python
import numpy as np
from truefalsepython import nrow, ncol, colMeans, rowMeans, colSums, rowSums, apply, lapply, sapply, sample, sample_int


np.random.seed(1)

# some 2D array
random_matrix = np.random.randint(8, size = (5, 3))


# how to get rows and cols counts
print(nrow(random_matrix)) # 5

print(ncol(random_matrix)) # 3

# operations for each row/column
print(rowMeans(random_matrix))
# [4.         2.66666667 5.         0.33333333 5.33333333]

print(colMeans(random_matrix))
# [2.4 4.4 3.6]

print(rowSums(random_matrix))
# [12  8 15  1 16]

print(colSums(random_matrix))
# [12 22 18]

# apply function (MARGIN is 1 for rows and 2 for columns)
print(apply(random_matrix, MARGIN = 1, FUN = np.min))
# [3 0 3 0 4]

# as u can see, it's not necessary to use FUN returns only 1 number by vector
print(apply(random_matrix, MARGIN = 2, FUN = np.sqrt))
#[[2.23606798 0.         1.73205081 0.         2.        ]
# [1.73205081 2.64575131 2.23606798 0.         2.64575131]
# [2.         1.         2.64575131 1.         2.23606798]]

some_arr = np.array([1, 2, 3, 5, 4, 3, 2])

# returns list
print(lapply(some_arr, lambda x: -x))
# [-1, -2, -3, -5, -4, -3, -2]

# returns numpy array
print(sapply(some_arr, lambda x: -x))
# [-1 -2 -3 -5 -4 -3 -2]

# like np.random.choice but replace = False by default
print(sample(some_arr, 4))
# [5 3 2 1]

# sample numbers from 0 to n-1
print(sample_int(n = 100, size = 10))
# [69 46 58 12 73 98 31 53 65 96]
```

