import scipy.stats
samples = [0.1, 0.2, 0.3, 6.1, 6.2, 6.3]
result = scipy.stats.circstd(samples=samples, nan_policy='propagate')
