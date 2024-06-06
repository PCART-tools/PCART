import numpy as np
a = np.array([[10, 7, 4], [3, 2, 1]])
result = np.percentile(a, [25, 50, 75], None, out=None, overwrite_input=False, method='linear')
print(result)
