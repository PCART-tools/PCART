import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
result = np.ma.average(a, axis=None, weights=None, returned=False)
