import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
result = np.sum(a, axis=1, dtype=np.float64, out=None, keepdims=True, initial=5)
