import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, imputation_order='ascending', initial_strategy='mean', sample_posterior=False, missing_values=0, n_nearest_features=None, max_iter=10, tol=0.001, keep_empty_features=False)
