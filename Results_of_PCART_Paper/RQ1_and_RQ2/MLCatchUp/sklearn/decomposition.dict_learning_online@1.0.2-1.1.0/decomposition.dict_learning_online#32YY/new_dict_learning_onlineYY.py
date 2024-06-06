from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_iter=100, iter_offset=0, dict_init=None, batch_size=3, random_state=None, inner_stats=None, n_jobs=None, return_inner_stats=False, verbose=False, alpha=1, method='lars', return_code=True, callback=None, shuffle=True, max_iter=None, tol=0.001, max_no_improvement=10)
