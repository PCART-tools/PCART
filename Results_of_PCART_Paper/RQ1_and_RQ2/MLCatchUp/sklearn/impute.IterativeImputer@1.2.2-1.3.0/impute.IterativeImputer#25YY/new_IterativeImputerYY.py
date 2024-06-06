import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(max_value=0, imputation_order='ascending', tol=0.001, initial_strategy='mean', min_value=(- 0), verbose=0, sample_posterior=False, missing_values=0, skip_complete=False, n_nearest_features=None, max_iter=10, fill_value=None)
