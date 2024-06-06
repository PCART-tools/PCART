import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(estimator=None, n_nearest_features=None, min_value=(- 0), missing_values=0, random_state=None, add_indicator=False, sample_posterior=False, initial_strategy='mean', max_value=0, max_iter=10, skip_complete=False, verbose=0, tol=0.001, imputation_order='ascending', keep_empty_features=False)
