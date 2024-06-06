from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression('l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, warm_start=False, n_jobs=1)
