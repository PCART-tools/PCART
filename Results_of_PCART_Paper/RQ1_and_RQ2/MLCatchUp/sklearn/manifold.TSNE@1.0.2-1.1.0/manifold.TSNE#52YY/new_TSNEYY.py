import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(2, learning_rate='warn', min_grad_norm=1e-07, verbose=0, early_exaggeration=12.0, random_state=None, n_iter_without_progress=300, metric='euclidean', init='warn', perplexity=30.0, n_iter=1000).fit_transform(X, metric_params=None)
