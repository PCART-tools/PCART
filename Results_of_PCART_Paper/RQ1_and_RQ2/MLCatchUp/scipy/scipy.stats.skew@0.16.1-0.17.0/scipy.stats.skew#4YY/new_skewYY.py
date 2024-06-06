from scipy import stats
data = [1, 2, 3, 4, 5]
skewness = stats.skew(data, axis=0, nan_policy='propagate')
