from scipy import stats
data = [1, 2, 3, 4, 5]
skewness = stats.skew(a=data, axis=0, bias=True, nan_policy='propagate')
