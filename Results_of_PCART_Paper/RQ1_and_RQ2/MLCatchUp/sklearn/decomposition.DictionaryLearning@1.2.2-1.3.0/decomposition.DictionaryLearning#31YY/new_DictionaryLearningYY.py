import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import DictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42, data_transposed=False)
dict_learner = DictionaryLearning(random_state=None, transform_n_nonzero_coefs=None, split_sign=False, n_jobs=None, tol=1e-08, transform_alpha=None, max_iter=1000, alpha=1, positive_code=False, transform_algorithm='omp', code_init=None, dict_init=None, fit_algorithm='lars', verbose=False, positive_dict=False, callback=None)
