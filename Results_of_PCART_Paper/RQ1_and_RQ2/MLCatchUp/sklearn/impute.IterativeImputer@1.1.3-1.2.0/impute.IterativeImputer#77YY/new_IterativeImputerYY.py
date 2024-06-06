import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(estimator=None, tol=0.001, min_value=(- 0), random_state=None, n_nearest_features=None, verbose=0, initial_strategy='mean', max_value=0, max_iter=10, skip_complete=False, missing_values=0, imputation_order='ascending', sample_posterior=False, keep_empty_features=False)
