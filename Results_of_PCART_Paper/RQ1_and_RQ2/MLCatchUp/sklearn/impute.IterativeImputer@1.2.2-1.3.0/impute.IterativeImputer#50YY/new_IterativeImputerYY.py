import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, missing_values=0, sample_posterior=False, skip_complete=False, imputation_order='ascending', n_nearest_features=None, max_iter=10, tol=0.001, initial_strategy='mean', fill_value=None)
