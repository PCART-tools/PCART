from scipy.stats import spearmanr
result = spearmanr([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], axis=0, nan_policy='propagate')
