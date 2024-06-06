import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(random_state=None, min_grad_norm=1e-07, learning_rate='warn', verbose=0, early_exaggeration=12.0, init='warn', n_iter_without_progress=300, perplexity=30.0, n_components=2, n_iter=1000, metric='euclidean').fit_transform(X, metric_params=None)
