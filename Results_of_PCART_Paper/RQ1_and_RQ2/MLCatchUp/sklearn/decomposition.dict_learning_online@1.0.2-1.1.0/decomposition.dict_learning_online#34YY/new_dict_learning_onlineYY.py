from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, dict_init=None, verbose=False, method='lars', positive_dict=False, batch_size=3, n_jobs=None, alpha=1, return_n_iter=False, shuffle=True, n_iter=100, inner_stats=None, return_code=True, iter_offset=0, callback=None, return_inner_stats=False, random_state=None, max_iter=None, tol=0.001, max_no_improvement=10)
