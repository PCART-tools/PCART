import scipy.stats
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 4, 5]
result = scipy.stats.linregress(x, y, alternative='two-sided')
