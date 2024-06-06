import scipy.stats
x = [13, 8, 12, 15, 8]
y = [10, 9, 7, 12, 11]
result = scipy.stats.ansari(x, y=y, alternative='two-sided')
result
