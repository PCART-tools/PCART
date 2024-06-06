from scipy import stats
a = [2, 2, 3, 5, 7, 2, 5, 6, 8, 9]
z = stats.zscore(a, 0, nan_policy='propagate')
