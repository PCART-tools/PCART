import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, n_nearest_features=None, skip_complete=False, initial_strategy='mean', max_iter=10, imputation_order='ascending', sample_posterior=False, missing_values=0, tol=0.001, keep_empty_features=False)
