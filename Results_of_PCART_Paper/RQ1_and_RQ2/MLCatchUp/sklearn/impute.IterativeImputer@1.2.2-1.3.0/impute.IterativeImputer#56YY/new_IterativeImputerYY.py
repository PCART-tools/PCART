import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, verbose=0, keep_empty_features=False, sample_posterior=False, initial_strategy='mean', add_indicator=False, imputation_order='ascending', missing_values=0, random_state=None, max_iter=10, max_value=0, min_value=(- 0), tol=0.001, n_nearest_features=None, skip_complete=False, fill_value=None)
