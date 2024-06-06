from scipy.stats import mstats
a = [[1, 2, 3], [4, 5, 6]]
result = mstats.variation(a, 0, ddof=0)
