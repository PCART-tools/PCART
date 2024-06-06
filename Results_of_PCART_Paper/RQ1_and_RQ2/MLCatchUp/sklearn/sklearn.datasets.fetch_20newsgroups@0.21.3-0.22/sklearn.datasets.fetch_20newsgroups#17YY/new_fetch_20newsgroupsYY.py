from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(None, 'train', None, True, random_state=42, return_X_y=False)
