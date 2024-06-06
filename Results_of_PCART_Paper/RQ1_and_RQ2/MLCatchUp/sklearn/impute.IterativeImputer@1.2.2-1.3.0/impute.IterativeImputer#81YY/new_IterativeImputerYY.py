import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(max_iter=10, initial_strategy='mean', missing_values=0, verbose=0, n_nearest_features=None, estimator=None, tol=0.001, imputation_order='ascending', skip_complete=False, max_value=0, min_value=(- 0), sample_posterior=False, fill_value=None)
