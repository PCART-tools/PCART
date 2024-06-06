import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(initial_strategy='mean', missing_values=0, max_iter=10, imputation_order='ascending', sample_posterior=False, n_nearest_features=None, tol=0.001, keep_empty_features=False)
