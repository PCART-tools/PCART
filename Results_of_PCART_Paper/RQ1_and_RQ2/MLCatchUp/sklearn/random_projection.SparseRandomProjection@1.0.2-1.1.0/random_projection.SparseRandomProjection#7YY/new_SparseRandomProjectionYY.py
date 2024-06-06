import numpy as np
from sklearn.random_projection import SparseRandomProjection
rng = np.random.RandomState(42)
X = rng.rand(25, 3000)
transformer = SparseRandomProjection(eps=0.1, density='auto', dense_output=False, compute_inverse_components=False)
