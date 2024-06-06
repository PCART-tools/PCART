import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, initial_strategy='mean', missing_values=0, sample_posterior=False, max_iter=10, min_value=(- 0), n_nearest_features=None, skip_complete=False, max_value=0, verbose=0, tol=0.001, imputation_order='ascending', keep_empty_features=False)
