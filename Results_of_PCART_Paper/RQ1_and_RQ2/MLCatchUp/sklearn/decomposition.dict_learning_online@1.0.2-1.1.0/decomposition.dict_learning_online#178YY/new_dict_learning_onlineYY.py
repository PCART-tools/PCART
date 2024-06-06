from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(n_iter=100, method='lars', batch_size=3, return_n_iter=False, dict_init=None, return_code=True, return_inner_stats=False, positive_dict=False, iter_offset=0, n_components=2, callback=None, alpha=1, verbose=False, n_jobs=None, shuffle=True, X=X, inner_stats=None, random_state=None, max_iter=None, tol=0.001, max_no_improvement=10)
