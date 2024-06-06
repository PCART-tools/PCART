from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier('log_loss', early_stopping='auto', max_iter=100, learning_rate=0.1, max_leaf_nodes=31, max_depth=None, l2_regularization=0.0, monotonic_cst=None, warm_start=False, min_samples_leaf=20, max_bins=255, categorical_features=None, interaction_cst=None, class_weight=None)
