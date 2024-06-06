import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])
result = np.stack(arrays=(array1, array2, array3), axis=1, out=None)
