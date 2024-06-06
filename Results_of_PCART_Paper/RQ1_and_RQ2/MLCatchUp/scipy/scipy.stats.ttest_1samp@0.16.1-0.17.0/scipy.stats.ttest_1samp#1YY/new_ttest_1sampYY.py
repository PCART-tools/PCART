import scipy.stats as stats
result = stats.ttest_1samp([10, 20, 30, 40, 50], 30, nan_policy='propagate')
