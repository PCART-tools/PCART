from scipy.stats import variation
a = [1.0, 2.0, 3.0, 4.0, 5.0]
result = variation(a=a, axis=0, nan_policy='propagate', ddof=0)
