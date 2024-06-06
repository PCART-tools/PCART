from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_components=2, callback=None, random_state=None, return_inner_stats=False, dict_init=None, method='lars', alpha=1, inner_stats=None, return_code=True, n_iter=100, n_jobs=None, batch_size=3, shuffle=True, iter_offset=0, verbose=False, max_iter=None, tol=0.001, max_no_improvement=10)
