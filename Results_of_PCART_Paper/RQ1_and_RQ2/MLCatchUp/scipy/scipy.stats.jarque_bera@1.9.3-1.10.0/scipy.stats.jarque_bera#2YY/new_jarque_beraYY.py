from scipy.stats import jarque_bera
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = jarque_bera(x=x, axis=None, nan_policy='propagate', keepdims=False)
