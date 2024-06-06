import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(n_nearest_features=None, max_iter=10, initial_strategy='mean', imputation_order='ascending', sample_posterior=False, missing_values=0, tol=0.001, min_value=(- 0), skip_complete=False, fill_value=None)
