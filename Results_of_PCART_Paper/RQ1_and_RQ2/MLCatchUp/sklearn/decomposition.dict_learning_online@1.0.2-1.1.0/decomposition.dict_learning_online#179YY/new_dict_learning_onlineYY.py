from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(method='lars', n_iter=100, verbose=False, positive_dict=False, return_n_iter=False, callback=None, iter_offset=0, shuffle=True, n_jobs=None, X=X, random_state=None, batch_size=3, n_components=2, positive_code=False, inner_stats=None, alpha=1, return_code=True, dict_init=None, return_inner_stats=False, max_iter=None, tol=0.001, max_no_improvement=10)
