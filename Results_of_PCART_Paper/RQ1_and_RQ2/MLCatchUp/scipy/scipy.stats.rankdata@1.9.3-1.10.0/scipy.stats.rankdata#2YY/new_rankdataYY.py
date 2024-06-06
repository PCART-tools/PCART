import numpy as np
from scipy.stats import rankdata
a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
result = rankdata(a, axis=None, nan_policy='propagate')
