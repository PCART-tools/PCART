from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, 2, method='lars', batch_size=3, callback=None, n_iter=100, n_jobs=None, iter_offset=0, alpha=1, shuffle=True, verbose=False, random_state=None, dict_init=None, return_code=True, max_iter=None, tol=0.001, max_no_improvement=10)
