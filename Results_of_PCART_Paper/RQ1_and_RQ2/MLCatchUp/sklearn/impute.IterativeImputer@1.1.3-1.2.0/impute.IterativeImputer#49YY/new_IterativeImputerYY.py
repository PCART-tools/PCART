import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, n_nearest_features=None, sample_posterior=False, max_value=0, max_iter=10, min_value=(- 0), tol=0.001, initial_strategy='mean', missing_values=0, skip_complete=False, imputation_order='ascending', keep_empty_features=False)
