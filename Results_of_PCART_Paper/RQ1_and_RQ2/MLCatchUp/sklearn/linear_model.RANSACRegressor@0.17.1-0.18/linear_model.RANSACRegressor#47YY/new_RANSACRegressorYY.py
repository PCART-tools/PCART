from sklearn.linear_model import RANSACRegressor
reg = RANSACRegressor(None, None, None, None, None, 100, 0, 0, stop_probability=0.99, loss='absolute_loss')
