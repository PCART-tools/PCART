from PIL import ImageOps, Image
image = Image.open('/home/zhang/example.jpg')
result = ImageOps.autocontrast(image, 0, ignore=None, preserve_tone=False)
