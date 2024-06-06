from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(iter_offset=0, shuffle=True, random_state=None, verbose=False, method='lars', alpha=1, n_components=2, dict_init=None, return_code=True, n_jobs=None, batch_size=3, X=X, callback=None, n_iter=100, max_iter=None, tol=0.001, max_no_improvement=10)
