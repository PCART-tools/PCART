from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(return_n_iter=False, verbose=False, positive_dict=False, positive_code=False, random_state=None, callback=None, shuffle=True, return_code=True, method='lars', batch_size=3, n_jobs=None, X=X, inner_stats=None, iter_offset=0, n_iter=100, alpha=1, dict_init=None, return_inner_stats=False, max_iter=None, tol=0.001, max_no_improvement=10)
