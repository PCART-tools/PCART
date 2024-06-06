import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(missing_values=0, imputation_order='ascending', initial_strategy='mean', sample_posterior=False, tol=0.001, max_iter=10, n_nearest_features=None, fill_value=None)
