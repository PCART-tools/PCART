import lightgbm as lgb
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
(X, y) = (iris.data, iris.target)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.2, random_state=42)
train_data = lgb.Dataset(X_train, label=y_train)
param = {'num_leaves': 31, 'objective': 'multiclass', 'num_classes': 3}
bst = lgb.train(param, train_data, 10)
model_json = bst.dump_model(None, start_iteration=0, object_hook=None)
