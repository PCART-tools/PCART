from scipy.stats import kurtosistest
data = [0.585, 0.742, 0.575, 0.719, 0.613]
result = kurtosistest(data, 0, nan_policy='propagate', alternative='two-sided')
