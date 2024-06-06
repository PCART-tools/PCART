from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
(X, y) = make_regression(n_samples=200, random_state=1)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, random_state=1)
regr = MLPRegressor((100,), 'relu', 'adam', 0.0001, 'auto', 'constant', 0.001, 0.5, 500, True, 1, 0.0001, False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9).fit(X_train, y_train, max_fun=15000)
