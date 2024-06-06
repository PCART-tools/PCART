import numpy as np
from scipy.optimize import shgo

def func(x):
    return x[0] * x[1] * x[2]
bounds = [(1, 5), (1, 5), (1, 5)]
result = shgo(func, bounds, (), None, None, 1, None, {'options': {'maxfev': 100}}, options=None, sampling_method='simplicial', workers=1)
print(result.fun)
