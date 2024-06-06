import scipy.stats
a = [1, 2, 2, 3, 3, 3]
skewness = scipy.stats.skew(a, 0, True, 'propagate', keepdims=False)
