from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', categorical_features=None, max_depth=None, min_samples_leaf=20, max_iter=100, max_bins=255, max_leaf_nodes=31, l2_regularization=0.0, learning_rate=0.1, interaction_cst=None, class_weight=None)
