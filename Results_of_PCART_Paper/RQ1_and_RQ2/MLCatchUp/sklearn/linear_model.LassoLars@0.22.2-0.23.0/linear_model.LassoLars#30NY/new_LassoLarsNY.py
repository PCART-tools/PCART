from sklearn import linear_model
reg = linear_model.LassoLars(1.0, eps=2.220446049250313e-16, fit_intercept=True, verbose=False, normalize=True, precompute='auto', max_iter=500, jitter=None, random_state=None)
