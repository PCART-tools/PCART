import numpy as np
from sklearn.metrics import jaccard_similarity_score
y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
jaccard_similarity_score(y_true, y_pred=y_pred, normalize=True, sample_weight=None)
