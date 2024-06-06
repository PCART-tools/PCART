from sklearn import metrics
y_true = [1, 0, 1, 1, 0, 1]
y_pred = [0.9, 0.1, 0.8, 0.4, 0.6, 0.9]
metrics.log_loss(y_true, y_pred, 1e-15, True, sample_weight=None)
