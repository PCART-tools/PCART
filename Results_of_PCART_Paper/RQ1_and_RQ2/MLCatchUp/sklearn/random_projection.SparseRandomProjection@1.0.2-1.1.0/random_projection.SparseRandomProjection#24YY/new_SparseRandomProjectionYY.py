import numpy as np
from sklearn.random_projection import SparseRandomProjection
rng = np.random.RandomState(42)
X = rng.rand(25, 3000)
transformer = SparseRandomProjection(random_state=rng, density='auto', dense_output=False, eps=0.1, n_components='auto', compute_inverse_components=False)
