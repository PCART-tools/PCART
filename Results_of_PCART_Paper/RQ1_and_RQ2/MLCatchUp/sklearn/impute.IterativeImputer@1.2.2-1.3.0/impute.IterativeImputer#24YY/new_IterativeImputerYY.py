import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(imputation_order='ascending', missing_values=0, initial_strategy='mean', tol=0.001, n_nearest_features=None, max_value=0, max_iter=10, min_value=(- 0), sample_posterior=False, skip_complete=False, fill_value=None)
