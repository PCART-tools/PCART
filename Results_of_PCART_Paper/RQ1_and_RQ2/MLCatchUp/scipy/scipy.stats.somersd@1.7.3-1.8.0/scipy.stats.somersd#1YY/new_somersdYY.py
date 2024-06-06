import scipy.stats
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
result = scipy.stats.somersd(x, y, initial_lexsort=None, nan_policy='propagate', method='auto', variant='b', alternative='two-sided')
