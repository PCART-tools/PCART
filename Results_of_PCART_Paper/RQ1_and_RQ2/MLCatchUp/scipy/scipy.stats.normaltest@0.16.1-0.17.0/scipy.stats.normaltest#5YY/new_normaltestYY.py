import numpy as np
from scipy import stats
a = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
result = stats.normaltest(a=a, axis=0, nan_policy='propagate')
