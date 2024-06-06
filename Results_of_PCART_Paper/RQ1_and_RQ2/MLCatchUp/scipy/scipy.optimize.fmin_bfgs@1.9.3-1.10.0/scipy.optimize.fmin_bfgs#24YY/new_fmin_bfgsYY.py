from scipy.optimize import fmin_bfgs
import numpy as np

def f(x):
    return x[0] ** 2 + x[1] ** 2
x0 = [2, 2]
result = fmin_bfgs(f, x0=x0, fprime=None, args=(), gtol=1e-05, norm=np.inf, xrtol=0)
result
