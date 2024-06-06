import scipy.stats
result = scipy.stats.tmin(a=[1, 2, 3, 4, 5], lowerlimit=2, axis=0, inclusive=True, nan_policy='propagate')
