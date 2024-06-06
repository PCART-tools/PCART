from PIL import Image
img = Image.open('/home/zhang/example.jpg')
rotated_img = img.rotate(45, Image.BICUBIC, True, (100, 100), translate=(20, 30), fillcolor=None)
