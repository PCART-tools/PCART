import numpy as np
from sklearn.calibration import calibration_curve
y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
y_pred = np.array([0.1, 0.2, 0.3, 0.4, 0.65, 0.7, 0.8, 0.9, 1.0])
(prob_true, prob_pred) = calibration_curve(y_true, strategy='uniform', y_prob=y_pred, pos_label=None)
