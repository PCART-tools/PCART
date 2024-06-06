from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_iris
(X, y) = load_iris(return_X_y=True)
clf = HistGradientBoostingClassifier(max_iter=100, l2_regularization=0.0, learning_rate=0.1, min_samples_leaf=20, loss='log_loss', max_bins=255, max_leaf_nodes=31, categorical_features=None, max_depth=None, interaction_cst=None, class_weight=None)
