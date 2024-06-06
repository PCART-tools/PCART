import scipy.signal
wp = 0.2
ws = 0.3
gpass = 1
gstop = 40
cheb1ord_result = scipy.signal.cheb1ord(wp=wp, ws=ws, gpass=gpass, gstop=gstop, fs=None)
