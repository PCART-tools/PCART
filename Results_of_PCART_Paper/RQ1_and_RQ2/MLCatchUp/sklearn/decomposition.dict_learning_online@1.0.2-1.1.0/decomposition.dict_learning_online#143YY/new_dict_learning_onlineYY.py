from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, iter_offset=0, n_iter=100, positive_code=False, return_code=True, alpha=1, callback=None, verbose=False, inner_stats=None, method='lars', random_state=None, shuffle=True, dict_init=None, batch_size=3, positive_dict=False, return_inner_stats=False, n_components=2, n_jobs=None, return_n_iter=False, max_iter=None, tol=0.001, max_no_improvement=10)
