import scipy.stats
data = [1, 2, 3, 4, 5]
result = scipy.stats.kstatvar(data, 2, axis=None, nan_policy='propagate', keepdims=False)
