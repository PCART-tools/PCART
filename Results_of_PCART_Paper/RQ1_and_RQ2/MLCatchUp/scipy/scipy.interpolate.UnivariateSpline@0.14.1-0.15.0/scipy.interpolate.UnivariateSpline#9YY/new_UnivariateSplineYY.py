import numpy as np
from scipy.interpolate import UnivariateSpline
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.1, 0.5, 0.9, 0.6, 0.2])
spline = UnivariateSpline(x, y, None, bbox=[None, None], ext=0)
