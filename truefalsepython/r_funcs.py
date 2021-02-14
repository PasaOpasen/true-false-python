
import numpy as np


from .logical import TRUE, FALSE, NULL



def ifelse(logical_vector, if_true, if_false):
    return np.where(logical_vector, if_true, if_false)



def nrow(arr2D):
    """
    returns number of rows
    """
    return arr2D.shape[0]

def ncol(arr2D):
    """
    returns number of columns
    """
    return arr2D.shape[1]



def rowSums(arr2D):
    """
    returns sums for each row
    """
    return np.sum(arr2D, axis = 1)

def colSums(arr2D):
    """
    returns sums for each column
    """    
    return np.sum(arr2D, axis = 0)


def rowMeans(arr2D):
    """
    returns average for each row
    """
    return np.mean(arr2D, axis = 1)

def colMeans(arr2D):
    """
    returns average for each column
    """
    return np.mean(arr2D, axis = 0)



def apply(arr2D, MARGIN, FUN):
    """
    applies function FUN to dimension of arr2D array (for rows if MARGIN == 1 and columns if MARGIN == 2) 
    """

    if MARGIN == 1:
        return np.array([FUN(arr2D[i, :]) for i in range(nrow(arr2D))])
    elif MARGIN == 2:
        return np.array([FUN(arr2D[:, i]) for i in range(ncol(arr2D))])
    else:
        raise Exception(f"MARGIN param must be 1 for rows and 2 for columns, not {MARGIN}")


def lapply(array, func):
    """
    applies function func for each element in array (array/list or something else)
    """
    return list(map(func, array)) # faster than [func(a) for a in array] over 1.5 times

def sapply(array, func):
    """
    like lapply but returns numpy array
    """
    return np.array(lapply(array, func))


def sample(array, size, replace = False, prob = None):
    """
    it is np.random.choice but replace = False by default
    """
    return np.random.choice(array, size, replace = replace, p = prob)


def sample_int(n, size = 'same', replace = FALSE, prob = NULL):
    """
    sample numbers from 0 to n-1
    """
    return np.random.choice(n, n if size == 'same' else size, replace = replace, p = prob)









