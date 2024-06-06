import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import DictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42, data_transposed=False)
dict_learner = DictionaryLearning(None, transform_alpha=None, split_sign=False, positive_dict=False, tol=1e-08, verbose=False, n_jobs=None, fit_algorithm='lars', code_init=None, alpha=1, transform_max_iter=1000, transform_n_nonzero_coefs=None, dict_init=None, transform_algorithm='omp', max_iter=1000, random_state=None, positive_code=False, callback=None)
