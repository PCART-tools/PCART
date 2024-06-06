from sklearn import linear_model
reg = linear_model.Lars(normalize=True, precompute='auto', n_nonzero_coefs=500, fit_intercept=True, verbose=False, jitter=None, random_state=None)
