from scipy.stats import skewtest
a = [1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0]
result = skewtest(a, 0, nan_policy='propagate', alternative='two-sided')
result
