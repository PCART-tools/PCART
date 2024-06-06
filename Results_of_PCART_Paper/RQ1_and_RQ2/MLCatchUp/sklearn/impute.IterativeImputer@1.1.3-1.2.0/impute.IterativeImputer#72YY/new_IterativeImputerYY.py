import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(n_nearest_features=None, max_iter=10, tol=0.001, missing_values=0, estimator=None, initial_strategy='mean', imputation_order='ascending', sample_posterior=False, keep_empty_features=False)
