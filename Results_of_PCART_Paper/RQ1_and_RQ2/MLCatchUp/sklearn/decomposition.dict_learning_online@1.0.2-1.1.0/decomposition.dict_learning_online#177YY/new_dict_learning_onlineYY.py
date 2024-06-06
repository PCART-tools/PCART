from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(shuffle=True, iter_offset=0, batch_size=3, X=X, n_components=2, alpha=1, n_iter=100, method='lars', return_n_iter=False, verbose=False, callback=None, dict_init=None, random_state=None, inner_stats=None, return_inner_stats=False, return_code=True, n_jobs=None, max_iter=None, tol=0.001, max_no_improvement=10)
