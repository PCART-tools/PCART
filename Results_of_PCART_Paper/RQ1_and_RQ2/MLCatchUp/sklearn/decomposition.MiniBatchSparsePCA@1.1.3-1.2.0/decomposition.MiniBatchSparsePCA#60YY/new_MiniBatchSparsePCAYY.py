import numpy as np
from sklearn.datasets import make_friedman1
from sklearn.decomposition import MiniBatchSparsePCA
(X, _) = make_friedman1(n_samples=200, n_features=30, random_state=0)
transformer = MiniBatchSparsePCA(shuffle=True, callback=None, verbose=False, batch_size=50, n_jobs=None, alpha=1, method='lars', ridge_alpha=0.01, n_components=5, random_state=0, n_iter=100, max_iter=None, tol=0.001, max_no_improvement=10)
