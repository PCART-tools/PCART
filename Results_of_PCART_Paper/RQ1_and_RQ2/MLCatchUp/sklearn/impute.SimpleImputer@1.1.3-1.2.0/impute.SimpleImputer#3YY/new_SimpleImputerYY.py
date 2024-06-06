import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(strategy='mean', keep_empty_features=False)
