import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c
xdata = np.array([0, 1, 2, 3, 4, 5])
ydata = np.array([0.5, 0.4, 0.3, 0.1, 0.05, 0.02])
(popt, _) = curve_fit(func, xdata, ydata, (1.0, 1.0, 1.0), absolute_sigma=False)
