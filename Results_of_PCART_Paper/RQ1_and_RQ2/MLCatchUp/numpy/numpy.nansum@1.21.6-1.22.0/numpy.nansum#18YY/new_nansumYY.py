import numpy as np
a = np.array([[1, 2], [3, np.nan]])
result = np.nansum(a,  0, dtype=np.float64, out=None, keepdims=False)
