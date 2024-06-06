import numpy as np
from sklearn.metrics import precision_recall_curve
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
(precision, recall, thresholds) = precision_recall_curve(sample_weight=None, y_true=y_true, probas_pred=y_scores, drop_intermediate=False)
