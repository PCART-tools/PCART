import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
result = np.stack((a, b, c), dtype=None, casting='same_kind')
