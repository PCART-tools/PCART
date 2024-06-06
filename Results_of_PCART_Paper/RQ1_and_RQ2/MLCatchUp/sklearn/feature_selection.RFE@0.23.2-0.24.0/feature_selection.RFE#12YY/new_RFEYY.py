from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFE
from sklearn.svm import SVR
(X, y) = make_friedman1(n_samples=50, n_features=10, random_state=0)
estimator = SVR(kernel='linear')
selector = RFE(n_features_to_select=5, estimator=estimator, step=1, verbose=0, importance_getter='auto')
