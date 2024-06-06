from scipy.stats import tmax
result = tmax(a=[1, 2, 3, 4, 5], upperlimit=4, axis=0, inclusive=True, nan_policy='propagate')
