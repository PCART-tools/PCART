import numpy as np
p = np.array([0, 1, 3, 6, 9, 12, 15, 18, 21])
result = np.unwrap(p, 10, 0, period=6.283185307179586)
