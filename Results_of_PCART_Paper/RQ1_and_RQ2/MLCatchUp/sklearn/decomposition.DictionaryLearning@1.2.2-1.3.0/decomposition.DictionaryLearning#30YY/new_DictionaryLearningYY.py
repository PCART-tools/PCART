import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import DictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42, data_transposed=False)
dict_learner = DictionaryLearning(verbose=False, random_state=None, alpha=1, code_init=None, tol=1e-08, n_jobs=None, fit_algorithm='lars', split_sign=False, transform_alpha=None, transform_n_nonzero_coefs=None, max_iter=1000, dict_init=None, positive_code=False, transform_algorithm='omp', callback=None)
