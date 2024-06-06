import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, imputation_order='ascending', n_nearest_features=None, missing_values=0, sample_posterior=False, initial_strategy='mean', max_iter=10, max_value=0, skip_complete=False, tol=0.001, min_value=(- 0), fill_value=None)
