from scipy.optimize import fmin_bfgs
import numpy as np

def f(x):
    return x[0] ** 2 + x[1] ** 2
x0 = [2, 2]
result = fmin_bfgs(f, x0, None, (), 1e-05, np.inf, epsilon=1.4901161193847656e-08, maxiter=None, full_output=0, disp=1, xrtol=0)
result
