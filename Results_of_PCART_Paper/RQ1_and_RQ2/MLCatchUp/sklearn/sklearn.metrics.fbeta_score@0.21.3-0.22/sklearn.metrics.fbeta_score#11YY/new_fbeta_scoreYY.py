import numpy as np
from sklearn.metrics import fbeta_score
y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
fbeta_score(y_true, y_pred, 0.1, None, pos_label=1, average='macro', sample_weight=None, zero_division='warn')
