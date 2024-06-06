import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(imputation_order='ascending', sample_posterior=False, tol=0.001, max_iter=10, min_value=(- 0), n_nearest_features=None, estimator=None, initial_strategy='mean', missing_values=0, skip_complete=False, fill_value=None)
