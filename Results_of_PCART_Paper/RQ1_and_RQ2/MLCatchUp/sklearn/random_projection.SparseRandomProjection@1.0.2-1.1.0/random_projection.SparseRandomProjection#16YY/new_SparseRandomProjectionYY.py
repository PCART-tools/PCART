import numpy as np
from sklearn.random_projection import SparseRandomProjection
rng = np.random.RandomState(42)
X = rng.rand(25, 3000)
transformer = SparseRandomProjection('auto', density='auto', random_state=rng, dense_output=False, eps=0.1, compute_inverse_components=False)
