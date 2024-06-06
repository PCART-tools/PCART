import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(2, learning_rate='warn', n_iter_without_progress=300, min_grad_norm=1e-07, verbose=0, n_iter=1000, random_state=None, init='warn', square_distances='legacy', n_jobs=None, early_exaggeration=12.0, perplexity=30.0, method='barnes_hut', angle=0.5, metric='euclidean').fit_transform(X, metric_params=None)
