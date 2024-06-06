import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, max_value=0, imputation_order='ascending', max_iter=10, verbose=0, n_nearest_features=None, missing_values=0, min_value=(- 0), initial_strategy='mean', add_indicator=False, sample_posterior=False, tol=0.001, skip_complete=False, random_state=None, fill_value=None)
