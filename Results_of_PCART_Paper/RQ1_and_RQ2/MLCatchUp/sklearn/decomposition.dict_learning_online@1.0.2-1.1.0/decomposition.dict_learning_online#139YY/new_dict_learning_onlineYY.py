from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, verbose=False, batch_size=3, random_state=None, return_inner_stats=False, shuffle=True, callback=None, iter_offset=0, n_components=2, alpha=1, return_code=True, n_jobs=None, n_iter=100, method='lars', dict_init=None, max_iter=None, tol=0.001, max_no_improvement=10)
