import numpy as np
from scipy.stats import kurtosis
data = np.array([1, 2, 3, 4, 5])
result = kurtosis(data, 0, fisher=True, nan_policy='propagate')
