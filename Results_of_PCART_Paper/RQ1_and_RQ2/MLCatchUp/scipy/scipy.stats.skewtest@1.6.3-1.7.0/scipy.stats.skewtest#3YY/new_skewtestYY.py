from scipy.stats import skewtest
a = [1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0]
result = skewtest(a, 0, alternative='two-sided')
result
