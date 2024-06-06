import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import DictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42, data_transposed=False)
dict_learner = DictionaryLearning(transform_n_nonzero_coefs=None, dict_init=None, verbose=False, transform_algorithm='omp', alpha=1, code_init=None, fit_algorithm='lars', n_components=None, tol=1e-08, random_state=None, n_jobs=None, transform_alpha=None, max_iter=1000, split_sign=False, callback=None)
