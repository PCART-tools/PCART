from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(verbose=False, alpha=1, return_code=True, batch_size=3, callback=None, n_iter=100, X=X, dict_init=None, n_components=2, max_iter=None, tol=0.001, max_no_improvement=10)
