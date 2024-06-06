from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(dict_init=None, return_code=True, n_iter=100, batch_size=3, n_components=2, X=X, verbose=False, alpha=1, shuffle=True, callback=None, max_iter=None, tol=0.001, max_no_improvement=10)
