from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
(X, y) = make_regression(n_samples=200, random_state=1)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, random_state=1)
regr = MLPRegressor((100,), 'relu', solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=500, shuffle=True).fit(X_train, y_train, max_fun=15000)
