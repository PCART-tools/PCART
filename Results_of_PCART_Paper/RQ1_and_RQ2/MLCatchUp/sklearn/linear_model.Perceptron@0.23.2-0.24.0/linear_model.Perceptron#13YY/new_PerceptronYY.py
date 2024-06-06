from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(validation_fraction=0.1, l1_ratio=0.15)
