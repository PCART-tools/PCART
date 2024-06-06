import numpy as np
from scipy.stats import hmean
data = np.array([[1, 2, 3], [4, 5, 6]])
result = hmean(data, axis=0, dtype=float, weights=None, nan_policy='propagate', keepdims=False)
