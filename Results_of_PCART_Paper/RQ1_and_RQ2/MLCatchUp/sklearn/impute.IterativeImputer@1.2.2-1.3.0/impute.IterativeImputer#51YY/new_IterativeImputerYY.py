import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, tol=0.001, imputation_order='ascending', max_iter=10, sample_posterior=False, missing_values=0, min_value=(- 0), n_nearest_features=None, skip_complete=False, initial_strategy='mean', fill_value=None)
