from PIL import Image
img = Image.open('/home/zhang/example.jpg')
rotated_img = img.rotate(45, Image.BICUBIC, expand=True, center=(100, 100), fillcolor=None)
