import scipy.stats
samples = [0.1, 0.2, 0.3, 6.1, 6.2, 6.3]
result = scipy.stats.circstd(samples, 6.283185307179586, nan_policy='propagate')
