from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', monotonic_cst=None, learning_rate=0.1, max_leaf_nodes=31, max_depth=None, l2_regularization=0.0, max_iter=100, max_bins=255, min_samples_leaf=20, categorical_features=None, interaction_cst=None, class_weight=None)
