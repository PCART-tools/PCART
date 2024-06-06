import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
result = np.ones_like(a, int, order='K', subok=True, shape=None)
