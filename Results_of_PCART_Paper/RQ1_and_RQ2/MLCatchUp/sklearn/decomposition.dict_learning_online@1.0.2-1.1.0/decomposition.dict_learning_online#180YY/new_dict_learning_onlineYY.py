from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(shuffle=True, positive_code=False, dict_init=None, alpha=1, X=X, method_max_iter=1000, positive_dict=False, inner_stats=None, n_jobs=None, batch_size=3, return_n_iter=False, iter_offset=0, verbose=False, return_inner_stats=False, n_iter=100, return_code=True, callback=None, method='lars', n_components=2, random_state=None, max_iter=None, tol=0.001, max_no_improvement=10)
