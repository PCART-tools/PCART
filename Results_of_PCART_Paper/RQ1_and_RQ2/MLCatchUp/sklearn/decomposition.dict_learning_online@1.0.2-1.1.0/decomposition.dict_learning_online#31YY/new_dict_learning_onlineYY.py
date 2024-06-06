from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_iter=100, shuffle=True, random_state=None, return_code=True, dict_init=None, method='lars', verbose=False, callback=None, n_jobs=None, iter_offset=0, return_inner_stats=False, alpha=1, batch_size=3, max_iter=None, tol=0.001, max_no_improvement=10)
