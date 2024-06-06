from scipy import stats
data = [1, 2, 3, 4, 5]
skewness = stats.skew(a=data, nan_policy='propagate')
