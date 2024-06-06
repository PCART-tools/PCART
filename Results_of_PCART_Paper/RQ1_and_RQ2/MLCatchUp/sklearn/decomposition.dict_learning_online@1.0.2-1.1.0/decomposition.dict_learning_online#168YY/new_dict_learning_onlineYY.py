from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(batch_size=3, dict_init=None, n_components=2, X=X, alpha=1, callback=None, n_iter=100, return_code=True, max_iter=None, tol=0.001, max_no_improvement=10)
