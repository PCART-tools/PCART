from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, 2, verbose=False, iter_offset=0, return_code=True, batch_size=3, alpha=1, shuffle=True, method='lars', callback=None, n_iter=100, n_jobs=None, dict_init=None, return_inner_stats=False, random_state=None, max_iter=None, tol=0.001, max_no_improvement=10)
