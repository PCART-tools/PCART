from scipy import stats
result = stats.kendalltau([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], True, nan_policy='propagate')
