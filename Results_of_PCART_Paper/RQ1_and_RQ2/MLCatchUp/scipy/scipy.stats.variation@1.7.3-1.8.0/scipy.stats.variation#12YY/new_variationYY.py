from scipy.stats import variation
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = variation(a, 0, nan_policy='propagate', ddof=0, keepdims=False)
