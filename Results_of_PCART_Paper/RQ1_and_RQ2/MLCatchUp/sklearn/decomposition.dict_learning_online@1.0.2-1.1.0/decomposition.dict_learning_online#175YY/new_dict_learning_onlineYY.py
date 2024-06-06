from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(return_inner_stats=False, shuffle=True, iter_offset=0, verbose=False, n_iter=100, n_jobs=None, return_code=True, batch_size=3, callback=None, method='lars', n_components=2, X=X, alpha=1, random_state=None, dict_init=None, max_iter=None, tol=0.001, max_no_improvement=10)
