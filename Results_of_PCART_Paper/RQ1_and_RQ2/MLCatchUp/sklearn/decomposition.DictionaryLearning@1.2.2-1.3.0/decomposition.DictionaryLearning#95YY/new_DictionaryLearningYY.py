import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import DictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42, data_transposed=False)
dict_learner = DictionaryLearning(n_jobs=None, random_state=None, transform_alpha=None, alpha=1, transform_n_nonzero_coefs=None, code_init=None, max_iter=1000, positive_dict=False, tol=1e-08, dict_init=None, verbose=False, positive_code=False, n_components=None, split_sign=False, fit_algorithm='lars', transform_algorithm='omp', callback=None)
