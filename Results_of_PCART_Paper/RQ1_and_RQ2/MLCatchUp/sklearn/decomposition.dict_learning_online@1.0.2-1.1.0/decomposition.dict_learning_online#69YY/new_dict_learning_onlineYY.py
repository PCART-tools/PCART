from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(n_jobs=None, dict_init=None, return_inner_stats=False, verbose=False, batch_size=3, n_iter=100, random_state=None, iter_offset=0, X=X, callback=None, method='lars', inner_stats=None, return_code=True, return_n_iter=False, shuffle=True, alpha=1, max_iter=None, tol=0.001, max_no_improvement=10)
