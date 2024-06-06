from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(max_iter=100, monotonic_cst=None, categorical_features=None, max_bins=255, learning_rate=0.1, loss='log_loss', l2_regularization=0.0, max_depth=None, max_leaf_nodes=31, warm_start=False, min_samples_leaf=20, interaction_cst=None, class_weight=None)
