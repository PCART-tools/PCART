from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
(X, y) = make_friedman1(n_samples=50, n_features=10, random_state=0)
estimator = SVR(kernel='linear')
selector = RFECV(cv=5, estimator=estimator, scoring=None, step=1, min_features_to_select=1, verbose=0, importance_getter='auto')
