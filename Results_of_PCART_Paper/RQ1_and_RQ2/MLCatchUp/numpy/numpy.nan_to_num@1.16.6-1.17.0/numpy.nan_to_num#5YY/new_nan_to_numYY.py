import numpy as np
x = np.array([1.0, np.nan, 2.0, np.inf, -np.inf])
result = np.nan_to_num(x=x, copy=False, nan=0.0, posinf=None, neginf=None)
