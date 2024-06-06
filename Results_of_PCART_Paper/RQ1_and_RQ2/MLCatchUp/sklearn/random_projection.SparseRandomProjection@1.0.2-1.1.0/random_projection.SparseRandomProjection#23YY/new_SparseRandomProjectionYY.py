import numpy as np
from sklearn.random_projection import SparseRandomProjection
rng = np.random.RandomState(42)
X = rng.rand(25, 3000)
transformer = SparseRandomProjection(density='auto', dense_output=False, n_components='auto', eps=0.1, compute_inverse_components=False)
