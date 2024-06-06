import numpy as np
from scipy.linalg import norm
a = np.array([[1, 2, 3], [4, 5, 6]])
result = norm(a=a, ord=2, axis=None, keepdims=False, check_finite=True)
