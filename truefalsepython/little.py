
from typing import Any

def is_number(x: Any):
    try:
        return bool(0 == x*0)
    except:
        return False


def is_even(x : float):
    return x % 2 == 0


def is_odd(x: float):
    return not is_even(x)



def min_fast(a: Any, b: Any):
    '''
    1.5 times faster than row min(a, b)
    '''
    return  a if a < b else b

def max_fast(a: Any, b: Any):
    return a if a > b else b

