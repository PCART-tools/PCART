from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, return_n_iter=False, verbose=False, random_state=None, return_inner_stats=False, method='lars', callback=None, batch_size=3, alpha=1, n_jobs=None, inner_stats=None, dict_init=None, return_code=True, shuffle=True, positive_dict=False, n_iter=100, positive_code=False, iter_offset=0, max_iter=None, tol=0.001, max_no_improvement=10)
