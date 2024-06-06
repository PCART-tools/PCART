import scipy.signal
x = [1, 2, 3, 4, 5]
up = 2
down = 3
axis = 0
window = ('kaiser', 5.0)
result = scipy.signal.resample_poly(x, up, down, axis, window, padtype='constant', cval=None)
