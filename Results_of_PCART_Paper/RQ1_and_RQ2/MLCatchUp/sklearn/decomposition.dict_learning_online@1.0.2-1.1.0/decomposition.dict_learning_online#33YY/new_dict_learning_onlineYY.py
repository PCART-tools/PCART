from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, random_state=None, inner_stats=None, alpha=1, return_inner_stats=False, n_iter=100, dict_init=None, shuffle=True, iter_offset=0, batch_size=3, callback=None, method='lars', n_jobs=None, verbose=False, return_code=True, return_n_iter=False, max_iter=None, tol=0.001, max_no_improvement=10)
