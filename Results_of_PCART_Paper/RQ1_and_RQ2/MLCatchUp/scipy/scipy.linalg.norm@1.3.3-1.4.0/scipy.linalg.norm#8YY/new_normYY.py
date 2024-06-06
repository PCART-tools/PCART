import numpy as np
from scipy.linalg import norm
a = np.array([[1, 2, 3], [4, 5, 6]])
result = norm(a, ord=2, axis=None, check_finite=True)
