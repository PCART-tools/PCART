from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(method='lars', return_n_iter=False, shuffle=True, dict_init=None, iter_offset=0, verbose=False, random_state=None, n_jobs=None, batch_size=3, inner_stats=None, return_code=True, positive_dict=False, alpha=1, callback=None, return_inner_stats=False, X=X, n_iter=100, max_iter=None, tol=0.001, max_no_improvement=10)
