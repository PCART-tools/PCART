from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(loss='log_loss', min_samples_leaf=20, max_depth=None, max_bins=255, max_leaf_nodes=31, l2_regularization=0.0, learning_rate=0.1, max_iter=100, interaction_cst=None, class_weight=None)
