from scipy import stats
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]
result = stats.ttest_ind(a, b, 0, equal_var=True, permutations=None, random_state=None, trim=0)
