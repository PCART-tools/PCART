import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(max_iter=10, estimator=None, skip_complete=False, missing_values=0, initial_strategy='mean', n_nearest_features=None, imputation_order='ascending', sample_posterior=False, tol=0.001, fill_value=None)
