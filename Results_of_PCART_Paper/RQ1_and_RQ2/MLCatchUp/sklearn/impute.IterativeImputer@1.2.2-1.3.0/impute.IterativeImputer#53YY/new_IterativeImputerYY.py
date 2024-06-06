import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, missing_values=0, initial_strategy='mean', imputation_order='ascending', verbose=0, n_nearest_features=None, sample_posterior=False, max_iter=10, min_value=(- 0), tol=0.001, skip_complete=False, max_value=0, fill_value=None)
