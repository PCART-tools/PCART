from sklearn import linear_model
clf = linear_model.BayesianRidge(300, 0.001, 1e-06, 1e-06, 1e-06, 1e-06, compute_score=False, alpha_init=None, lambda_init=None)
