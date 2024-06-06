from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(l2_regularization=0.0, loss='log_loss', interaction_cst=None, class_weight=None)
