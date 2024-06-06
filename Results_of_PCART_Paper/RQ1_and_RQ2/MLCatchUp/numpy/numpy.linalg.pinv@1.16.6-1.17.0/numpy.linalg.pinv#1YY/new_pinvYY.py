import numpy as np
a = np.array([[1, 2], [3, 4]])
result = np.linalg.pinv(a, hermitian=False)
