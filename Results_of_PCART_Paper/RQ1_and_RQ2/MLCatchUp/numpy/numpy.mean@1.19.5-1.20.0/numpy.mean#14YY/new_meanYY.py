import numpy as np
a = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
result = np.mean(a=a, axis=1, dtype=np.float64, out=None)
