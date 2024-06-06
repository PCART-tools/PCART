from sklearn import linear_model
reg = linear_model.Lars(fit_intercept=True, verbose=False, normalize=True, precompute='auto', n_nonzero_coefs=500, eps=2.220446049250313e-16, jitter=None, random_state=None)
