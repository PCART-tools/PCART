from scipy.stats import circmean
samples = [0.1, 0.2, 6.0, 6.1]
result = circmean(samples=samples, nan_policy='propagate')
print(result)
