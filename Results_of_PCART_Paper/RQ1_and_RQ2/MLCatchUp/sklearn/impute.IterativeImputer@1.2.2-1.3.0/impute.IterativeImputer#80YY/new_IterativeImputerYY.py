import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(estimator=None, initial_strategy='mean', max_value=0, imputation_order='ascending', missing_values=0, sample_posterior=False, min_value=(- 0), tol=0.001, n_nearest_features=None, skip_complete=False, max_iter=10, fill_value=None)
