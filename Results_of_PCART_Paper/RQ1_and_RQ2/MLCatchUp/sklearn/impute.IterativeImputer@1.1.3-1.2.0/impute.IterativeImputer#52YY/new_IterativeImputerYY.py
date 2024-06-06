import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, n_nearest_features=None, add_indicator=False, initial_strategy='mean', verbose=0, missing_values=0, random_state=None, max_iter=10, sample_posterior=False, min_value=(- 0), imputation_order='ascending', tol=0.001, max_value=0, skip_complete=False, keep_empty_features=False)
