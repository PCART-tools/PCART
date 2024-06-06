from scipy.stats import binom_test
result = binom_test(x=7, n=10, p=0.5, alternative='two-sided')
