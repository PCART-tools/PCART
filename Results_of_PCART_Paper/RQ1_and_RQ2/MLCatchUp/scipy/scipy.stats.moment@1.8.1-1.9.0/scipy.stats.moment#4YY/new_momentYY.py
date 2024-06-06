import scipy.stats as stats
a = [1, 2, 3, 4, 5]
moment_result = stats.moment(a, moment=2, keepdims=False)
