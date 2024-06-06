from scipy import stats
data = [1, 2, 3, 4, 5]
skewness = stats.skew(data, 0, True, nan_policy='propagate')
