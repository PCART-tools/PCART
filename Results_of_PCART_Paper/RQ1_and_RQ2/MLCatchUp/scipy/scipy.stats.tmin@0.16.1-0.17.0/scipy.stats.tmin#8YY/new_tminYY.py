import scipy.stats
result = scipy.stats.tmin([1, 2, 3, 4, 5], lowerlimit=2, axis=0, nan_policy='propagate')
