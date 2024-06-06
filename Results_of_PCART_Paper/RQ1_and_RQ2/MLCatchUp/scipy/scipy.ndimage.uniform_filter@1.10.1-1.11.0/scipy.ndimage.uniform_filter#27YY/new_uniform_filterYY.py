import scipy.ndimage
input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
size = (2, 2)
output = None
mode = 'reflect'
cval = 0.0
origin = 0
result = scipy.ndimage.uniform_filter(input=input, size=size, output=output, mode=mode, cval=cval, origin=origin, axes=None)
