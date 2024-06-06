import numpy as np
from scipy.stats.mstats import winsorize
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
limits = [0.1, 0.2]
inclusive = (False, True)
result = winsorize(data, limits, inclusive, False, nan_policy='propagate')
