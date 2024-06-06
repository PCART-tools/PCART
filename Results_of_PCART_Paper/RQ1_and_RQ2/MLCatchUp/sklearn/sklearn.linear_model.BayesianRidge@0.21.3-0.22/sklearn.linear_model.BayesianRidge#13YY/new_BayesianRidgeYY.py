from sklearn import linear_model
clf = linear_model.BayesianRidge(300, 0.001, alpha_1=1e-06, alpha_2=1e-06, alpha_init=None, lambda_init=None)
