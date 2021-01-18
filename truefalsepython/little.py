


def is_number(x):
    try:
        return bool(0 == x*0)
    except:
        return False


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return not is_even(x)
