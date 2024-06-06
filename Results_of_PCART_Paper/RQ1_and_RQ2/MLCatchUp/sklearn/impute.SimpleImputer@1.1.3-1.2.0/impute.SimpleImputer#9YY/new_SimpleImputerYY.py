import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(strategy='mean', fill_value=None, missing_values=np.nan, keep_empty_features=False)
