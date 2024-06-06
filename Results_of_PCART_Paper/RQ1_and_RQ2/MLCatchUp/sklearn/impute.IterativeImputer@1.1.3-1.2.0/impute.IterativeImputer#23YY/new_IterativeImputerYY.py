import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(min_value=(- 0), sample_posterior=False, imputation_order='ascending', tol=0.001, missing_values=0, max_iter=10, n_nearest_features=None, initial_strategy='mean', skip_complete=False, max_value=0, keep_empty_features=False)
