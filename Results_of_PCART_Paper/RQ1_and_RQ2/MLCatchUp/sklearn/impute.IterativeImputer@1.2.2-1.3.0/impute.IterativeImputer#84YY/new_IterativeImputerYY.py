import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(max_iter=10, add_indicator=False, min_value=(- 0), random_state=None, skip_complete=False, n_nearest_features=None, keep_empty_features=False, tol=0.001, verbose=0, sample_posterior=False, missing_values=0, estimator=None, imputation_order='ascending', initial_strategy='mean', max_value=0, fill_value=None)
