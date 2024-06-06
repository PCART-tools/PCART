from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
confusion_matrix(y_true=y_true, y_pred=y_pred, labels=None, sample_weight=None, normalize=None)
