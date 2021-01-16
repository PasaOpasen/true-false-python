[![PyPI
version](https://badge.fury.io/py/truefalsepython.svg)](https://pypi.org/project/truefalsepython/)

# true-false-python

PyPI package with some better syntax tools for python


```
pip install truefalsepython
```

## Logical tools

For `True` and `False` values there are equal constants (like it is in C-like languages or R) `TRUE, T, true` and `FALSE, F, false`:

```python

from truefalsepython import TRUE, FALSE, T, F, true, false

print(True == T) # True
print(True == TRUE) # True
print(True == true) # True


print(False == F) # True
print(False == FALSE) # True
print(False == false) # True
```




