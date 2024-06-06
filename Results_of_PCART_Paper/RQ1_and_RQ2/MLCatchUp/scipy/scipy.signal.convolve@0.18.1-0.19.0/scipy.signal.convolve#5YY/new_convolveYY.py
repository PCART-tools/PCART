import scipy.signal
result = scipy.signal.convolve([1, 2, 3], [0.5, 0.25], mode='full', method='auto')
