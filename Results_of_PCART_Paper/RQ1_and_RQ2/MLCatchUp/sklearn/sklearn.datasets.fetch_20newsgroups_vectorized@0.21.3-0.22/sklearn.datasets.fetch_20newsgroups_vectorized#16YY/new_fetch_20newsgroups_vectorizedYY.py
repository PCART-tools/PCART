from sklearn.datasets import fetch_20newsgroups_vectorized
newsgroups_train = fetch_20newsgroups_vectorized('train', (), '/home/zhang/sklearn_data', True, False, normalize=True)
