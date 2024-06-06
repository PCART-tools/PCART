import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
min_value = np.min(a,  None,  None, keepdims=np._NoValue)
print(min_value)
