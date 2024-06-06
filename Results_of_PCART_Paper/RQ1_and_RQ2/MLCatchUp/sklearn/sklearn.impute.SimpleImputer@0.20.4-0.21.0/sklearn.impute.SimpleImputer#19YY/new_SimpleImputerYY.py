import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(np.nan, 'mean', fill_value=None, verbose=0, copy=True, add_indicator=False)
