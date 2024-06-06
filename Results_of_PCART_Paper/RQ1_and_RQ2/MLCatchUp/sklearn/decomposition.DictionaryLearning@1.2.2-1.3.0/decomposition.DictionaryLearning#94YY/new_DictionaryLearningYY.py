import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import DictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42, data_transposed=False)
dict_learner = DictionaryLearning(split_sign=False, transform_algorithm='omp', max_iter=1000, n_components=None, transform_alpha=None, random_state=None, dict_init=None, alpha=1, fit_algorithm='lars', transform_n_nonzero_coefs=None, verbose=False, positive_code=False, tol=1e-08, n_jobs=None, code_init=None, callback=None)
