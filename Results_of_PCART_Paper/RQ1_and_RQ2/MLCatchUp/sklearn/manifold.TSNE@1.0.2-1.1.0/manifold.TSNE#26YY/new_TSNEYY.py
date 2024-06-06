import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(n_iter_without_progress=300, random_state=None, min_grad_norm=1e-07, n_iter=1000, init='warn', learning_rate='warn', verbose=0, method='barnes_hut', metric='euclidean', perplexity=30.0, angle=0.5, early_exaggeration=12.0).fit_transform(X, metric_params=None)
