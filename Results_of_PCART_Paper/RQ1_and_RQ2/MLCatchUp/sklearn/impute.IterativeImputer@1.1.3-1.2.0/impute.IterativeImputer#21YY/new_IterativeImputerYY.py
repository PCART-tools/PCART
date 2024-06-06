import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(missing_values=0, initial_strategy='mean', max_iter=10, sample_posterior=False, skip_complete=False, n_nearest_features=None, imputation_order='ascending', tol=0.001, keep_empty_features=False)
