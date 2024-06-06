from sklearn.linear_model import Ridge
import numpy as np
(n_samples, n_features) = (10, 5)
np.random.seed(0)
y = np.random.randn(n_samples)
X = np.random.randn(n_samples, n_features)
clf = Ridge(1.0, True, False, True, None, 0.001, 'auto', random_state=None)
