import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(min_value=(- 0), imputation_order='ascending', max_iter=10, missing_values=0, tol=0.001, sample_posterior=False, initial_strategy='mean', skip_complete=False, n_nearest_features=None, keep_empty_features=False)
