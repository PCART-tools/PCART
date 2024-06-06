from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_jobs=None, batch_size=3, n_iter=100, alpha=1, method='lars', dict_init=None, verbose=False, return_code=True, callback=None, shuffle=True, iter_offset=0, random_state=None, max_iter=None, tol=0.001, max_no_improvement=10)
