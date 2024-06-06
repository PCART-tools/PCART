import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(verbose=0, skip_complete=False, n_nearest_features=None, max_value=0, missing_values=0, tol=0.001, sample_posterior=False, imputation_order='ascending', min_value=(- 0), initial_strategy='mean', estimator=None, max_iter=10, keep_empty_features=False)
