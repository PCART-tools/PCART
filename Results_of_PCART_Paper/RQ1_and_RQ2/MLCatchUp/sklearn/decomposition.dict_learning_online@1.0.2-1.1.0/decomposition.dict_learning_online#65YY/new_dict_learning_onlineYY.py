from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(batch_size=3, iter_offset=0, n_iter=100, shuffle=True, n_jobs=None, alpha=1, return_code=True, method='lars', callback=None, X=X, dict_init=None, verbose=False, max_iter=None, tol=0.001, max_no_improvement=10)
