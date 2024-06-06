import scipy.stats as stats
a = [5.1, 3.5, 1.4, 0.2]
b = [4.9, 3.0, 1.4, 0.2]
result = stats.ttest_rel(a, b, 0, nan_policy='propagate')
