from sklearn import linear_model
reg = linear_model.Lars(precompute='auto', n_nonzero_coefs=500, eps=2.220446049250313e-16, fit_intercept=True, verbose=False, normalize=True, jitter=None, random_state=None)
