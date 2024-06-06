import scipy.stats
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
result = scipy.stats.kendalltau(x, y, True, nan_policy='propagate', method='auto', alternative='two-sided')
