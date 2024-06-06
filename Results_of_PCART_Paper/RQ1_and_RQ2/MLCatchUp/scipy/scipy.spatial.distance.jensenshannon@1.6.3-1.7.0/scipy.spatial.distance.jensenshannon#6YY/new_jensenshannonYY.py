import numpy as np
from scipy.spatial.distance import jensenshannon
p = np.array([0.2, 0.4, 0.4])
q = np.array([0.1, 0.6, 0.3])
result = jensenshannon(p, q=q, base=None, axis=0, keepdims=False)
