
import sys
sys.path.append('..')

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


