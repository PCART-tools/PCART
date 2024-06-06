from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b):
    return a * x + b
xdata = [1.0, 2.0, 3.0, 4.0, 5.0]
ydata = [2.0, 3.9, 6.1, 8.2, 9.8]
p0 = [1.0, 1.0]
(params, covariance) = curve_fit(func, xdata, ydata=ydata, p0=p0, sigma=None, absolute_sigma=False, full_output=False)
(a, b) = params
print(f'a = {a}, b = {b}')
