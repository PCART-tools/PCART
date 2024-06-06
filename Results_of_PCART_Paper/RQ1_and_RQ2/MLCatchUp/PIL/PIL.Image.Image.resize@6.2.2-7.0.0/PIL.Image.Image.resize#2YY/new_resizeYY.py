from PIL import Image
image = Image.open('/home/zhang/example.jpg')
resized_image_resample = image.resize(size=(100, 100), reducing_gap=None)
