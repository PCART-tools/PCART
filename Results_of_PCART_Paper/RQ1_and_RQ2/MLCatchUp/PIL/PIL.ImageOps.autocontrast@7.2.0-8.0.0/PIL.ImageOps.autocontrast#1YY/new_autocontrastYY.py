from PIL import Image, ImageOps
image = Image.open('/home/zhang/example.jpg')
result_image = ImageOps.autocontrast(image, mask=None)
