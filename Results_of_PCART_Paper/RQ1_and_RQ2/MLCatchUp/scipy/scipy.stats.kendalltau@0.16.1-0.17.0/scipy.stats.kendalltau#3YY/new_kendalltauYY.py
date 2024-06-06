from scipy import stats
result = stats.kendalltau(x=[1, 2, 3, 4, 5], y=[5, 4, 3, 2, 1], nan_policy='propagate')
