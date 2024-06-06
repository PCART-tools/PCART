import numpy as np
from sklearn.datasets import make_sparse_coded_signal
from sklearn.decomposition import MiniBatchDictionaryLearning
(X, dictionary, code) = make_sparse_coded_signal(n_samples=100, n_components=15, n_features=20, n_nonzero_coefs=10, random_state=42)
dict_learner = MiniBatchDictionaryLearning(transform_algorithm='omp', alpha=1, n_iter=1000, dict_init=None, shuffle=True, verbose=False, n_jobs=None, fit_algorithm='lars', transform_n_nonzero_coefs=None, batch_size=3, transform_alpha=None, max_iter=None, callback=None, tol=0.001, max_no_improvement=10)
