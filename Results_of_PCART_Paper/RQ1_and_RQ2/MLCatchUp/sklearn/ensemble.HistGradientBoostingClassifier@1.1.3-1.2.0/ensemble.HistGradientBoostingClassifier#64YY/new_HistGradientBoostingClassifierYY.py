from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', validation_fraction=0.1, warm_start=False, learning_rate=0.1, early_stopping='auto', max_iter=100, categorical_features=None, max_bins=255, min_samples_leaf=20, scoring='loss', monotonic_cst=None, max_leaf_nodes=31, max_depth=None, l2_regularization=0.0, interaction_cst=None, class_weight=None)
