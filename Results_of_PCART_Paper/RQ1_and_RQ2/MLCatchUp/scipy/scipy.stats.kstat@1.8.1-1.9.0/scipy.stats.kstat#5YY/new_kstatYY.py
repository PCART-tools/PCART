import scipy.stats as stats
data = [1, 2, 3, 4, 5]
result = stats.kstat(data=data, n=2, axis=None, nan_policy='propagate', keepdims=False)
