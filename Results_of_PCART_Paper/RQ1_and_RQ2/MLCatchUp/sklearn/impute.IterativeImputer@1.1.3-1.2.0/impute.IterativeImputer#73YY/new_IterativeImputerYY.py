import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(initial_strategy='mean', skip_complete=False, estimator=None, max_iter=10, tol=0.001, sample_posterior=False, missing_values=0, imputation_order='ascending', n_nearest_features=None, keep_empty_features=False)
