import numpy as np
from sklearn.preprocessing import FunctionTransformer
transformer = FunctionTransformer(accept_sparse=False, validate=False, func=None, check_inverse=True, inverse_func=None, feature_names_out=None)
