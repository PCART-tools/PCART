from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, inner_stats=None, dict_init=None, iter_offset=0, method='lars', random_state=None, n_components=2, batch_size=3, alpha=1, return_code=True, n_iter=100, verbose=False, callback=None, n_jobs=None, return_n_iter=False, positive_dict=False, shuffle=True, return_inner_stats=False, max_iter=None, tol=0.001, max_no_improvement=10)
