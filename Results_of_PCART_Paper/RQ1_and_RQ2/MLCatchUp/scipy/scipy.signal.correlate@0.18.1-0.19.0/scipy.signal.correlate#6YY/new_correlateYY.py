import scipy.signal
result = scipy.signal.correlate([1, 2, 3, 4, 5], in2=[0.1, 0.2, 0.3], mode='full', method='auto')
