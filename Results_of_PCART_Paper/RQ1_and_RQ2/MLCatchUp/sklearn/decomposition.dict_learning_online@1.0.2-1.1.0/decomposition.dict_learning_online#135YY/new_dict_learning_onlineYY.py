from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_iter=100, n_components=2, shuffle=True, alpha=1, callback=None, verbose=False, batch_size=3, dict_init=None, return_code=True, n_jobs=None, max_iter=None, tol=0.001, max_no_improvement=10)
