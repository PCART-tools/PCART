from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(early_stopping='auto', loss='log_loss', warm_start=False, min_samples_leaf=20, categorical_features=None, monotonic_cst=None, l2_regularization=0.0, max_bins=255, max_leaf_nodes=31, validation_fraction=0.1, scoring='loss', max_depth=None, max_iter=100, learning_rate=0.1, interaction_cst=None, class_weight=None)
