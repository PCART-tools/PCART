import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(max_value=0, min_value=(- 0), skip_complete=False, n_nearest_features=None, sample_posterior=False, tol=0.001, initial_strategy='mean', random_state=None, verbose=0, add_indicator=False, missing_values=0, max_iter=10, imputation_order='ascending', keep_empty_features=False)
