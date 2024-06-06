from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(alpha=1, iter_offset=0, random_state=None, n_jobs=None, batch_size=3, return_inner_stats=False, dict_init=None, method='lars', X=X, callback=None, n_iter=100, return_code=True, shuffle=True, verbose=False, max_iter=None, tol=0.001, max_no_improvement=10)
