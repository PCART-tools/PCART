import numpy as np
from scipy.optimize import curve_fit

def model_function(x, a, b, c):
    return a * np.exp(-b * x) + c
xdata = np.array([0.1, 0.5, 1.0, 1.5, 2.0])
ydata = np.array([0.9, 0.6, 0.35, 0.2, 0.1])
p0 = [1.0, 1.0, 0.0]
(parameters, covariance) = curve_fit(model_function, p0=p0, absolute_sigma=False, ydata=ydata, full_output=False, xdata=xdata, bounds=((- np.inf), np.inf), check_finite=True, sigma=None, nan_policy=None)
print('Estimated Parameters:', parameters)
