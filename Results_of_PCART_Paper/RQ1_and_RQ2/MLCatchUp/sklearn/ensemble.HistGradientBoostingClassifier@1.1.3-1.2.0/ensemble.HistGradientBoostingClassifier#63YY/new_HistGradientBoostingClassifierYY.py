from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', scoring='loss', min_samples_leaf=20, max_depth=None, categorical_features=None, warm_start=False, max_iter=100, max_bins=255, monotonic_cst=None, max_leaf_nodes=31, learning_rate=0.1, l2_regularization=0.0, early_stopping='auto', interaction_cst=None, class_weight=None)
