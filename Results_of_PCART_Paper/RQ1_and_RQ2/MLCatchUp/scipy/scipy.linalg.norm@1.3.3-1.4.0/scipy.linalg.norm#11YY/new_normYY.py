import numpy as np
from scipy.linalg import norm
a = np.array([[1, 2, 3], [4, 5, 6]])
result = norm(a, 2, None, keepdims=False, check_finite=True)
