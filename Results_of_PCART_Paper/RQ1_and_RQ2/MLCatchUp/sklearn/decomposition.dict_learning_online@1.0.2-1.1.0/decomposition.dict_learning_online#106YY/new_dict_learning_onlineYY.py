from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, 2, batch_size=3, iter_offset=0, n_iter=100, return_n_iter=False, callback=None, inner_stats=None, n_jobs=None, method='lars', random_state=None, verbose=False, dict_init=None, alpha=1, return_inner_stats=False, shuffle=True, positive_dict=False, return_code=True, max_iter=None, tol=0.001, max_no_improvement=10)
