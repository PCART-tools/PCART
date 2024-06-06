from PIL import Image
image = Image.open('/home/zhang/example.jpg')
size = (300, 300)
method = Image.QUAD
data = (0, 0, 100, 0, 100, 100, 0, 100)
resample = Image.BILINEAR
fill = 1
transformed_image = image.transform(size, method, data, resample, fill=fill, fillcolor=None)
