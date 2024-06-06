from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(n_jobs=None, iter_offset=0, return_code=True, shuffle=True, method='lars', inner_stats=None, n_components=2, return_inner_stats=False, n_iter=100, callback=None, dict_init=None, verbose=False, random_state=None, X=X, alpha=1, batch_size=3, max_iter=None, tol=0.001, max_no_improvement=10)
