from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, 2, random_state=None, return_inner_stats=False, n_iter=100, callback=None, method_max_iter=1000, inner_stats=None, return_n_iter=False, iter_offset=0, positive_dict=False, alpha=1, return_code=True, dict_init=None, batch_size=3, positive_code=False, n_jobs=None, method='lars', verbose=False, shuffle=True, max_iter=None, tol=0.001, max_no_improvement=10)
