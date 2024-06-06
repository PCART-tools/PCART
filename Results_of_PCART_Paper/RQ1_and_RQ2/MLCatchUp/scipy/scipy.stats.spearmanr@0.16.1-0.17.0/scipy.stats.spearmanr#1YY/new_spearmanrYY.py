from scipy.stats import spearmanr
result = spearmanr([1, 2, 3, 4, 5], nan_policy='propagate')
