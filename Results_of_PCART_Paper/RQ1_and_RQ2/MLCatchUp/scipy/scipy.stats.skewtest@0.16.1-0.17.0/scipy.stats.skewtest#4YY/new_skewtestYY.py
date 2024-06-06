from scipy.stats import skewtest
result = skewtest([1.0, 2.0, 2.0, 3.0, 4.0, 4.0, 5.0, 6.0], axis=0, nan_policy='propagate')
