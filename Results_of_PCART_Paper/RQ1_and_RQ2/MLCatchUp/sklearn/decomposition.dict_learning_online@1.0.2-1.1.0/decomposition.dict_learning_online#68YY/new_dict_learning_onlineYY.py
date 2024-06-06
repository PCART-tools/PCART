from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(random_state=None, return_inner_stats=False, method='lars', X=X, batch_size=3, iter_offset=0, shuffle=True, n_iter=100, n_jobs=None, alpha=1, verbose=False, dict_init=None, return_code=True, callback=None, inner_stats=None, max_iter=None, tol=0.001, max_no_improvement=10)
