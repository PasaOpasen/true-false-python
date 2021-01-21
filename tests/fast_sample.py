
import sys
sys.path.append('..')

import numpy as np
from truefalsepython import fast_sample


random_arr = np.random.random(100)
random_probs = random_arr/random_arr.sum()


%timeit np.random.choice(random_arr, 1, p = random_probs)
# 72.9 µs ± 7.18 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%timeit fast_sample(random_arr, probs = random_probs)
# 31.4 µs ± 404 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)



