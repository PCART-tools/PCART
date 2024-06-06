from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, return_code=True, positive_dict=False, positive_code=False, random_state=None, n_jobs=None, method='lars', inner_stats=None, method_max_iter=1000, dict_init=None, alpha=1, return_n_iter=False, callback=None, n_iter=100, batch_size=3, shuffle=True, return_inner_stats=False, verbose=False, iter_offset=0, max_iter=None, tol=0.001, max_no_improvement=10)
