import numpy as np
from sklearn.random_projection import GaussianRandomProjection
rng = np.random.RandomState(42)
X = rng.rand(25, 3000)
transformer = GaussianRandomProjection('auto', eps=0.1, random_state=None, compute_inverse_components=False)
