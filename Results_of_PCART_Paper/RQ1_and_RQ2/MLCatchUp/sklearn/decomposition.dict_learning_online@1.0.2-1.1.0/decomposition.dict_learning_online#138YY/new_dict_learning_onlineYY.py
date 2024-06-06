from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, random_state=None, shuffle=True, verbose=False, n_iter=100, alpha=1, n_jobs=None, n_components=2, iter_offset=0, method='lars', callback=None, batch_size=3, return_code=True, dict_init=None, max_iter=None, tol=0.001, max_no_improvement=10)
