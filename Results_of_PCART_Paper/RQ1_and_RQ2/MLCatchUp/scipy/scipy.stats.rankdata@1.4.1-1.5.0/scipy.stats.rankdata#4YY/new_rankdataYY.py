import scipy.stats
a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = scipy.stats.rankdata(a, method='average', axis=None)
