import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(n_nearest_features=None, tol=0.001, max_iter=10, skip_complete=False, verbose=0, add_indicator=False, sample_posterior=False, min_value=(- 0), keep_empty_features=False, random_state=None, imputation_order='ascending', initial_strategy='mean', missing_values=0, max_value=0, fill_value=None)
