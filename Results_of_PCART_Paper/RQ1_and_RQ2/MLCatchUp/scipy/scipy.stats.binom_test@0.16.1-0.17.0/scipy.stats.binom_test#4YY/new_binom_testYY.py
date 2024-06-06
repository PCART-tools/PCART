from scipy.stats import binom_test
result = binom_test(7, 10, 0.5, alternative='two-sided')
