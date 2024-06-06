import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import DictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42, data_transposed=False)
dict_learner = DictionaryLearning(positive_dict=False, split_sign=False, positive_code=False, transform_alpha=None, transform_algorithm='omp', code_init=None, n_jobs=None, alpha=1, transform_max_iter=1000, max_iter=1000, verbose=False, transform_n_nonzero_coefs=None, dict_init=None, fit_algorithm='lars', random_state=None, tol=1e-08, callback=None)
