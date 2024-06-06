from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(learning_rate=0.1, max_leaf_nodes=31, l2_regularization=0.0, monotonic_cst=None, loss='log_loss', max_bins=255, categorical_features=None, max_iter=100, min_samples_leaf=20, max_depth=None, interaction_cst=None, class_weight=None)
