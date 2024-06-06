import scipy.stats as stats
a = [1, 2, 3, 4, 5]
moment_result = stats.moment(a, 2, 0, 'propagate', keepdims=False)
