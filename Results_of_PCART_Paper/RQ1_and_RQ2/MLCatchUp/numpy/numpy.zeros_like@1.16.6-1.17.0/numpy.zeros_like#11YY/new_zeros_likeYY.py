import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
result = np.zeros_like(a, float, 'C', subok=False, shape=None)
