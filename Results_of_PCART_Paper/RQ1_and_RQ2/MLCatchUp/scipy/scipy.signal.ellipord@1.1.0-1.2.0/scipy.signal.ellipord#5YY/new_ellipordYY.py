import scipy.signal
wp = 0.2
ws = 0.3
gpass = 3
gstop = 40
ellipord_result = scipy.signal.ellipord(wp=wp, ws=ws, gpass=gpass, gstop=gstop, fs=None)
