from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, 2, dict_init=None, batch_size=3, alpha=1, verbose=False, callback=None, iter_offset=0, shuffle=True, n_iter=100, return_code=True, method='lars', n_jobs=None, max_iter=None, tol=0.001, max_no_improvement=10)
