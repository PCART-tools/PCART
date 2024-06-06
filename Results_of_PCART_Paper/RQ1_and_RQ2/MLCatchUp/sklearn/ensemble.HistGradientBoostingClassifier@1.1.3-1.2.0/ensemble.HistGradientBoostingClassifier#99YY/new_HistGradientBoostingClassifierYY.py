from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(max_iter=100, min_samples_leaf=20, max_bins=255, l2_regularization=0.0, max_leaf_nodes=31, validation_fraction=0.1, categorical_features=None, loss='log_loss', scoring='loss', max_depth=None, monotonic_cst=None, warm_start=False, early_stopping='auto', learning_rate=0.1, n_iter_no_change=10, interaction_cst=None, class_weight=None)
