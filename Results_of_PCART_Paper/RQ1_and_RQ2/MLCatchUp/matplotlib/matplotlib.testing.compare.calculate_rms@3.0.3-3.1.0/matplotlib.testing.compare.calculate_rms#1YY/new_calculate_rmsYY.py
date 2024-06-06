from PIL import Image
import numpy as np
import matplotlib.testing.compare as mtc
expectedImage = np.array(Image.open('/home/zhang/example.png'))
actualImage = np.array(Image.open('/home/zhang/example.png'))
rms_error = mtc.calculate_rms(expectedImage,  actualImage)
