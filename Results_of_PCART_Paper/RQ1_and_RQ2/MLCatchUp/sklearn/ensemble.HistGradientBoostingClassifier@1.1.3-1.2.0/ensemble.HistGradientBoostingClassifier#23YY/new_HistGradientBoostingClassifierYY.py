from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(l2_regularization=0.0, max_leaf_nodes=31, learning_rate=0.1, max_depth=None, max_iter=100, min_samples_leaf=20, interaction_cst=None, class_weight=None)
