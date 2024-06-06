from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(dict_init=None, n_iter=100, method='lars', n_jobs=None, X=X, batch_size=3, shuffle=True, return_code=True, alpha=1, verbose=False, callback=None, max_iter=None, tol=0.001, max_no_improvement=10)
