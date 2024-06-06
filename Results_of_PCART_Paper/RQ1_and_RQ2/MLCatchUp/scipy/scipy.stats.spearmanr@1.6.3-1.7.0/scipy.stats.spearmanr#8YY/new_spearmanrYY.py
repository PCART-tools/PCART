from scipy.stats import spearmanr
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]
result = spearmanr(a, b, 0, 'propagate', alternative='two-sided')
print(result)
