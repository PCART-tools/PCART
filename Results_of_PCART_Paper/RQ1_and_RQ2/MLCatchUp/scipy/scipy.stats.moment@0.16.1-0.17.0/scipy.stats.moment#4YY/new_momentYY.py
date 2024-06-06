from scipy.stats import moment
a = [1, 2, 3, 4, 5]
result = moment(a, moment=1, nan_policy='propagate')
