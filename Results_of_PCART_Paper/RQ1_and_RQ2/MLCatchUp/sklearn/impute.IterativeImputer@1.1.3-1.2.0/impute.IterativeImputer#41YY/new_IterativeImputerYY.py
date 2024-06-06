import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, sample_posterior=False, missing_values=0, keep_empty_features=False)
