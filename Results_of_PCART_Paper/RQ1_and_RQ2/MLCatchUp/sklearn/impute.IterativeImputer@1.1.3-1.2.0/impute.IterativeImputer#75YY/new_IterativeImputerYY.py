import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(max_iter=10, skip_complete=False, estimator=None, max_value=0, sample_posterior=False, initial_strategy='mean', tol=0.001, n_nearest_features=None, imputation_order='ascending', min_value=(- 0), missing_values=0, keep_empty_features=False)
