import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
result = np.vstack((arr1, arr2, arr3), dtype=None, casting='same_kind')
