from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(verbose=False, return_code=True, X=X, shuffle=True, dict_init=None, batch_size=3, callback=None, n_iter=100, n_components=2, alpha=1, n_jobs=None, max_iter=None, tol=0.001, max_no_improvement=10)
