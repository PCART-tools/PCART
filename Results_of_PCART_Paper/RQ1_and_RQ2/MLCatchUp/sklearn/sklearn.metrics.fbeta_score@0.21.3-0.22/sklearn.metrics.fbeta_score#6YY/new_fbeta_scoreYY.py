import numpy as np
from sklearn.metrics import fbeta_score
y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
fbeta_score(y_true, y_pred=y_pred, beta=0.1, labels=None, pos_label=1, average='macro', zero_division='warn')
