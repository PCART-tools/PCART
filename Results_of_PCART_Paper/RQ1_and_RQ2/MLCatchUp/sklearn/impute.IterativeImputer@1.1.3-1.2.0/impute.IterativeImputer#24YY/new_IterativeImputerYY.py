import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(initial_strategy='mean', max_value=0, sample_posterior=False, skip_complete=False, min_value=(- 0), max_iter=10, tol=0.001, n_nearest_features=None, imputation_order='ascending', verbose=0, missing_values=0, keep_empty_features=False)
