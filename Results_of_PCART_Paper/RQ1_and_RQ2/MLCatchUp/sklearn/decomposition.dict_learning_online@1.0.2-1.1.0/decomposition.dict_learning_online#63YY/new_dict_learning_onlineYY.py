from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(n_iter=100, dict_init=None, n_jobs=None, verbose=False, return_code=True, shuffle=True, batch_size=3, X=X, alpha=1, callback=None, max_iter=None, tol=0.001, max_no_improvement=10)
