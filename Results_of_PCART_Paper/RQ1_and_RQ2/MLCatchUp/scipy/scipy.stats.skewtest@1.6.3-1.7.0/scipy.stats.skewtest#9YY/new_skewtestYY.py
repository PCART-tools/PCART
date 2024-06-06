from scipy.stats import skewtest
a = [1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0]
result = skewtest(a=a, axis=0, nan_policy='propagate', alternative='two-sided')
result
