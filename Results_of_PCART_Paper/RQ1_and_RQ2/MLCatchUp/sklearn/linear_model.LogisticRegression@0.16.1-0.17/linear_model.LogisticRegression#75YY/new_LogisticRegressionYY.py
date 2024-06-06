from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression('l2', False, 0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='liblinear', max_iter=100, multi_class='ovr', warm_start=False, n_jobs=1)
