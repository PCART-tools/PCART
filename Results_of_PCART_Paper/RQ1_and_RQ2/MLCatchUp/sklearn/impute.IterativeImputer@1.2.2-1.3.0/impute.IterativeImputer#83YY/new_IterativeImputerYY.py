import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(verbose=0, skip_complete=False, max_value=0, max_iter=10, sample_posterior=False, add_indicator=False, estimator=None, initial_strategy='mean', tol=0.001, min_value=(- 0), random_state=None, missing_values=0, imputation_order='ascending', n_nearest_features=None, fill_value=None)
