from PIL import Image
image = Image.open('/home/zhang/example.jpg')
resized_image_resample = image.resize((100, 100), resample=Image.BICUBIC, box=(10, 10, 110, 110), reducing_gap=None)
