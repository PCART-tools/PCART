from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, iter_offset=0, callback=None, batch_size=3, n_iter=100, n_jobs=None, verbose=False, n_components=2, method='lars', return_inner_stats=False, inner_stats=None, shuffle=True, return_n_iter=False, dict_init=None, alpha=1, random_state=None, return_code=True, max_iter=None, tol=0.001, max_no_improvement=10)
