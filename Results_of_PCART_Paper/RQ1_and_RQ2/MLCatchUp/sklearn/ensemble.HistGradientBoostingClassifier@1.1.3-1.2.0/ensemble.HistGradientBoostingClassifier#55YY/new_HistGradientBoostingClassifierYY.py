from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', learning_rate=0.1, max_depth=None, max_iter=100, max_leaf_nodes=31, interaction_cst=None, class_weight=None)
