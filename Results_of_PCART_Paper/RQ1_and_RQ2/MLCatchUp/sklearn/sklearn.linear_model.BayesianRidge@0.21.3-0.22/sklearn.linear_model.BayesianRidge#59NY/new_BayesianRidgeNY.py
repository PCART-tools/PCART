from sklearn import linear_model
clf = linear_model.BayesianRidge(300, 0.001, 1e-06, 1e-06, 1e-06, 1e-06, False, fit_intercept=True, normalize=False, copy_X=True, alpha_init=None, lambda_init=None)
