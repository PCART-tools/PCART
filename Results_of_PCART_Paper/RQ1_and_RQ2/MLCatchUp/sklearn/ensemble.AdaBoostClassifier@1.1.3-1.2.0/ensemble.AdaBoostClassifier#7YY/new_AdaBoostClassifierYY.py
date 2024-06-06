from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
(X, y) = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
clf = AdaBoostClassifier(algorithm='SAMME.R', n_estimators=100, learning_rate=1.0, estimator=None)
