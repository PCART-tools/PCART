import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, n_nearest_features=None, missing_values=0, sample_posterior=False, skip_complete=False, initial_strategy='mean', max_value=0, random_state=None, tol=0.001, min_value=(- 0), imputation_order='ascending', verbose=0, max_iter=10, keep_empty_features=False)
