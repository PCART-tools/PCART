import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(np.nan, 'mean', fill_value=None, add_indicator=False)
