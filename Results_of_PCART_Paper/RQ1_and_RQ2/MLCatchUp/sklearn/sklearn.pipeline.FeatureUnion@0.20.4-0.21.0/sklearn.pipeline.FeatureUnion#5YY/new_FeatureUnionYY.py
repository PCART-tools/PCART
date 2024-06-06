from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA, TruncatedSVD
union = FeatureUnion(transformer_list=[('pca', PCA(n_components=1)), ('svd', TruncatedSVD(n_components=2))], n_jobs=None, verbose=False)
