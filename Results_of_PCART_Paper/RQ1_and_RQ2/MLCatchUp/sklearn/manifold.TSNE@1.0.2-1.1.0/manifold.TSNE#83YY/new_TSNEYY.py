import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(method='barnes_hut', early_exaggeration=12.0, random_state=None, init='warn', angle=0.5, learning_rate='warn', min_grad_norm=1e-07, verbose=0, n_iter_without_progress=300, n_iter=1000, n_jobs=None, perplexity=30.0, metric='euclidean', n_components=2).fit_transform(X, metric_params=None)
