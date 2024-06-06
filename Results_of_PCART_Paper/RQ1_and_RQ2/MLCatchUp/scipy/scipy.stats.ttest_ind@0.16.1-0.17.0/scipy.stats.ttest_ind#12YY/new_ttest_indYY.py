import scipy.stats
result = scipy.stats.ttest_ind(a=[1, 2, 3, 4, 5], b=[2, 3, 4, 5, 6], axis=0, equal_var=True, nan_policy='propagate')
