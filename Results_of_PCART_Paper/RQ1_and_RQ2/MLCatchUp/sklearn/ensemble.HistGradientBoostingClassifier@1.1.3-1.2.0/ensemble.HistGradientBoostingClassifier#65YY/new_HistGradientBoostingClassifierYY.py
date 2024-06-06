from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', max_depth=None, warm_start=False, max_bins=255, monotonic_cst=None, max_iter=100, n_iter_no_change=10, min_samples_leaf=20, validation_fraction=0.1, learning_rate=0.1, categorical_features=None, max_leaf_nodes=31, early_stopping='auto', scoring='loss', l2_regularization=0.0, interaction_cst=None, class_weight=None)
