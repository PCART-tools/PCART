import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
q = 0.5
axis = None
out = None
overwrite_input = False
interpolation = 'linear'
keepdims = False
result = np.quantile(a=a, q=q, method='linear')
