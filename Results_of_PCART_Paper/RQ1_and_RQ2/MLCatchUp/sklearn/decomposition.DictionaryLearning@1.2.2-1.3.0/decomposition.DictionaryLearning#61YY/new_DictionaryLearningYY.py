import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import DictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42, data_transposed=False)
dict_learner = DictionaryLearning(None, random_state=None, n_jobs=None, code_init=None, fit_algorithm='lars', dict_init=None, max_iter=1000, tol=1e-08, transform_n_nonzero_coefs=None, transform_alpha=None, transform_algorithm='omp', verbose=False, split_sign=False, alpha=1, callback=None)
