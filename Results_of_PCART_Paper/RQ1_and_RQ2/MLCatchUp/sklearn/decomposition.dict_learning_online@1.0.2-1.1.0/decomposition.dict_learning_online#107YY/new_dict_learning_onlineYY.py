from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, 2, dict_init=None, random_state=None, method='lars', positive_code=False, return_n_iter=False, return_code=True, inner_stats=None, n_jobs=None, callback=None, verbose=False, positive_dict=False, alpha=1, batch_size=3, return_inner_stats=False, n_iter=100, iter_offset=0, shuffle=True, max_iter=None, tol=0.001, max_no_improvement=10)
