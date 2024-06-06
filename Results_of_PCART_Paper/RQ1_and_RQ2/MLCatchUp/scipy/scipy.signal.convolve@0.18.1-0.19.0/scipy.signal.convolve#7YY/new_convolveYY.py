import scipy.signal
result = scipy.signal.convolve(in1=[1, 2, 3], in2=[0.5, 0.25], mode='full', method='auto')
