import scipy.stats
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = scipy.stats.sem(a, nan_policy='propagate')
