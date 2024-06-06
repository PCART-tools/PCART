from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_iter=100, random_state=None, alpha=1, batch_size=3, dict_init=None, verbose=False, iter_offset=0, n_components=2, positive_dict=False, method='lars', positive_code=False, return_n_iter=False, shuffle=True, callback=None, return_inner_stats=False, inner_stats=None, n_jobs=None, return_code=True, method_max_iter=1000, max_iter=None, tol=0.001, max_no_improvement=10)
