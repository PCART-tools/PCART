from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', random_state=None, verbose=0, max_leaf_nodes=31, categorical_features=None, scoring='loss', max_depth=None, l2_regularization=0.0, learning_rate=0.1, n_iter_no_change=10, validation_fraction=0.1, warm_start=False, min_samples_leaf=20, max_bins=255, max_iter=100, tol=1e-07, early_stopping='auto', monotonic_cst=None, interaction_cst=None, class_weight=None)
