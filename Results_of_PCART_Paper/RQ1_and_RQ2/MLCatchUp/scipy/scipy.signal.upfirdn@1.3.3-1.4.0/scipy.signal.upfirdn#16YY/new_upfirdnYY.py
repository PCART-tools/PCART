from scipy.signal import upfirdn
h = [1, 2, 1]
x = [1, 2, 3, 4, 5, 6]
up = 2
down = 3
axis = -1
y = upfirdn(h, x, up=up, down=down, axis=axis, mode='constant', cval=0)
