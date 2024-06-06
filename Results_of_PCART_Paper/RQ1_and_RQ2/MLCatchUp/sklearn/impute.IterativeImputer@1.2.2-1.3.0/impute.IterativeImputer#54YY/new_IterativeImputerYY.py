import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, min_value=(- 0), sample_posterior=False, initial_strategy='mean', max_value=0, n_nearest_features=None, imputation_order='ascending', verbose=0, tol=0.001, missing_values=0, random_state=None, skip_complete=False, max_iter=10, fill_value=None)
