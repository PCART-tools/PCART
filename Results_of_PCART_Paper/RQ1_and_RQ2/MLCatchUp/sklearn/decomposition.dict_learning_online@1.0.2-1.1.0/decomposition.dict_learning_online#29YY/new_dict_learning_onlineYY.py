from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, method='lars', batch_size=3, iter_offset=0, callback=None, dict_init=None, n_iter=100, n_jobs=None, return_code=True, alpha=1, verbose=False, shuffle=True, max_iter=None, tol=0.001, max_no_improvement=10)
