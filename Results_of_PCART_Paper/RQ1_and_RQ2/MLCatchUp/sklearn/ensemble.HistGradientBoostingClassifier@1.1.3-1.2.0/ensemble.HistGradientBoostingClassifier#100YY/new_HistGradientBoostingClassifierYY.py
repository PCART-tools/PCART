from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(tol=1e-07, min_samples_leaf=20, max_depth=None, l2_regularization=0.0, loss='log_loss', n_iter_no_change=10, warm_start=False, validation_fraction=0.1, learning_rate=0.1, max_bins=255, categorical_features=None, max_iter=100, early_stopping='auto', max_leaf_nodes=31, scoring='loss', monotonic_cst=None, interaction_cst=None, class_weight=None)
