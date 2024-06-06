from scipy.interpolate import BSpline
import numpy as np
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
k = 3
t = np.array([0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 4.0, 4.0, 4.0, 4.0])
design_matrix = BSpline.design_matrix(x, t, k, extrapolate=False)
