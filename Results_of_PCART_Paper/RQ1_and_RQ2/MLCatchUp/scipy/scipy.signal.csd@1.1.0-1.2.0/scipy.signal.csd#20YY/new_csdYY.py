import scipy.signal
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
fs = 10.0
window = 'hann'
nperseg = None
noverlap = None
nfft = None
detrend = 'constant'
return_onesided = True
scaling = 'density'
axis = -1
result = scipy.signal.csd(x, y, fs, window, nperseg, noverlap=noverlap, average='mean')
