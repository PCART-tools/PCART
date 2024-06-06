from scipy import stats
samples = [0.1, 0.2, 1.0, 5.9, 6.0, 6.1, 6.2]
result = stats.circvar(samples, high=6.283185307179586, low=0, nan_policy='propagate')
print(result)
