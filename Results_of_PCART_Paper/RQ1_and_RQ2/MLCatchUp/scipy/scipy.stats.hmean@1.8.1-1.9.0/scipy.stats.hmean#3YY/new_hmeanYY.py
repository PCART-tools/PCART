import numpy as np
from scipy.stats import hmean
data = np.array([[1, 2, 3], [4, 5, 6]])
result = hmean(data, 0, weights=None, nan_policy='propagate', keepdims=False)
