import scipy.stats
import numpy as np
a = np.array([1, 2, 3, 4, 5])
result = scipy.stats.kurtosistest(a=a, nan_policy='propagate')
