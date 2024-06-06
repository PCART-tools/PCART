import numpy as np
from sklearn.datasets import make_friedman1
from sklearn.decomposition import MiniBatchSparsePCA
(X, _) = make_friedman1(n_samples=200, n_features=30, random_state=0)
transformer = MiniBatchSparsePCA(shuffle=True, ridge_alpha=0.01, verbose=False, callback=None, alpha=1, batch_size=50, n_iter=100, max_iter=None, tol=0.001, max_no_improvement=10)
