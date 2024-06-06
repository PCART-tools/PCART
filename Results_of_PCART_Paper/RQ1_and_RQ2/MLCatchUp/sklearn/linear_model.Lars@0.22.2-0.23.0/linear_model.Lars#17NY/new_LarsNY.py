from sklearn import linear_model
reg = linear_model.Lars(n_nonzero_coefs=500, fit_intercept=True, verbose=False, normalize=True, precompute='auto', jitter=None, random_state=None)
