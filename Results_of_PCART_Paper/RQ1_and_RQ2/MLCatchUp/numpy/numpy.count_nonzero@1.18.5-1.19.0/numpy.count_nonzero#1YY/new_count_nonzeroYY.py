import numpy as np
a = np.array([[1, 2, 0], [0, 4, 5], [6, 0, 8]])
result = np.count_nonzero(a, keepdims=False)
