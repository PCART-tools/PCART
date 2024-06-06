from scipy.stats import tmax
result = tmax([1, 2, 3, 4, 5], 4, axis=0, inclusive=True, nan_policy='propagate')
