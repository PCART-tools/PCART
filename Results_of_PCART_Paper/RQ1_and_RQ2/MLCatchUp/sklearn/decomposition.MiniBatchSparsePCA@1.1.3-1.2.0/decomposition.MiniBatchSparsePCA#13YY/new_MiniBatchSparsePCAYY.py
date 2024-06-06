import numpy as np
from sklearn.datasets import make_friedman1
from sklearn.decomposition import MiniBatchSparsePCA
(X, _) = make_friedman1(n_samples=200, n_features=30, random_state=0)
transformer = MiniBatchSparsePCA(n_iter=100, ridge_alpha=0.01, alpha=1, max_iter=None, tol=0.001, max_no_improvement=10)
