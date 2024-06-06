from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, return_code=True, alpha=1, n_iter=100, max_iter=None, tol=0.001, max_no_improvement=10)
