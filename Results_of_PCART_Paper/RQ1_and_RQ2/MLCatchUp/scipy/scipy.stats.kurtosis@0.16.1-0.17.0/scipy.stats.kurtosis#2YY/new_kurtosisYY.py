import numpy as np
from scipy.stats import kurtosis
data = np.array([1, 2, 3, 4, 5])
result = kurtosis(a=data, nan_policy='propagate')
