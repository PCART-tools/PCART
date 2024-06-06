import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(verbose=0, n_nearest_features=None, skip_complete=False, min_value=(- 0), max_iter=10, initial_strategy='mean', sample_posterior=False, tol=0.001, add_indicator=False, missing_values=0, imputation_order='ascending', random_state=None, max_value=0, fill_value=None)
