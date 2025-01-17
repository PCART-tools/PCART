from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(method='lars', X=X, callback=None, positive_code=False, return_n_iter=False, return_code=True, inner_stats=None, n_jobs=None, return_inner_stats=False, iter_offset=0, batch_size=3, positive_dict=False, verbose=False, random_state=None, shuffle=True, alpha=1, dict_init=None, method_max_iter=1000, n_iter=100, max_iter=None, tol=0.001, max_no_improvement=10)
