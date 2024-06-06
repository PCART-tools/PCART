import numpy as np
a = np.array([1.0, 2.0, np.nan, 4.0, 5.0])
result = np.nanvar(a=a, axis=None, dtype=None, out=None, ddof=0)
