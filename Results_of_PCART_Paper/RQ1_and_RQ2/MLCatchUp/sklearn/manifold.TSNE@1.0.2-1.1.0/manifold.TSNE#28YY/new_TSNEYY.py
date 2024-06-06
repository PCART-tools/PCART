import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(random_state=None, min_grad_norm=1e-07, n_iter=1000, early_exaggeration=12.0, metric='euclidean', square_distances='legacy', angle=0.5, verbose=0, init='warn', learning_rate='warn', n_iter_without_progress=300, method='barnes_hut', n_jobs=None, perplexity=30.0).fit_transform(X, metric_params=None)
