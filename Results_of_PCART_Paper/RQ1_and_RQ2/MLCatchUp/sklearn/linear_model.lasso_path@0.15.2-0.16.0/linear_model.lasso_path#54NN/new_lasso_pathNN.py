import numpy as np
from sklearn.linear_model import lasso_path
X = np.array([[1, 2, 3.1], [2.3, 5.4, 4.3]]).T
y = np.array([1, 2, 3.1])
coef_path = lasso_path(X,  y,  0.001,  100,  [5.0, 1.0, 0.5],  'auto',  None,  None,  None, copy_X=True)
