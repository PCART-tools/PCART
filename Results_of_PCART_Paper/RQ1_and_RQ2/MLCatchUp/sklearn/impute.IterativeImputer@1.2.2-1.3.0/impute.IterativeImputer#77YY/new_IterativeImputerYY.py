import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(estimator=None, n_nearest_features=None, tol=0.001, initial_strategy='mean', max_iter=10, imputation_order='ascending', missing_values=0, sample_posterior=False, fill_value=None)
