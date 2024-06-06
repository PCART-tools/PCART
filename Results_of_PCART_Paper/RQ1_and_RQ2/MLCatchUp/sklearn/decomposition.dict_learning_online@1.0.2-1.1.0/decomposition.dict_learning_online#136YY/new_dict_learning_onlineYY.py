from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_components=2, alpha=1, verbose=False, n_iter=100, batch_size=3, return_code=True, method='lars', dict_init=None, shuffle=True, callback=None, n_jobs=None, max_iter=None, tol=0.001, max_no_improvement=10)
