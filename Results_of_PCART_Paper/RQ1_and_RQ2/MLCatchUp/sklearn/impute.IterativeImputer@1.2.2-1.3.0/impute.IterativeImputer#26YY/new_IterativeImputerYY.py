import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(tol=0.001, initial_strategy='mean', skip_complete=False, missing_values=0, max_iter=10, verbose=0, min_value=(- 0), imputation_order='ascending', sample_posterior=False, n_nearest_features=None, max_value=0, random_state=None, fill_value=None)
