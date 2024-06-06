from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
(X, y) = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
clf = AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None, estimator=None)
