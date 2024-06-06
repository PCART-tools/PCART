import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(skip_complete=False, estimator=None, initial_strategy='mean', tol=0.001, imputation_order='ascending', missing_values=0, max_iter=10, n_nearest_features=None, min_value=(- 0), sample_posterior=False, keep_empty_features=False)
