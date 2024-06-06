from scipy.optimize import curve_fit

def f(x, a, b):
    return a * x + b
xdata = [1.0, 2.0, 3.0, 4.0, 5.0]
ydata = [2.0, 3.9, 6.1, 8.0, 10.2]
p0 = [1.0, 1.0]
(params, covariance) = curve_fit(f, xdata=xdata, ydata=ydata, p0=p0, sigma=None, absolute_sigma=False, check_finite=True, jac=None)
