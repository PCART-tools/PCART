import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(random_state=None, imputation_order='ascending', n_nearest_features=None, max_value=0, skip_complete=False, sample_posterior=False, verbose=0, min_value=(- 0), initial_strategy='mean', max_iter=10, missing_values=0, tol=0.001, keep_empty_features=False)
