from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, 2, callback=None, shuffle=True, iter_offset=0, alpha=1, random_state=None, method='lars', dict_init=None, n_iter=100, inner_stats=None, batch_size=3, n_jobs=None, return_code=True, return_inner_stats=False, verbose=False, max_iter=None, tol=0.001, max_no_improvement=10)
