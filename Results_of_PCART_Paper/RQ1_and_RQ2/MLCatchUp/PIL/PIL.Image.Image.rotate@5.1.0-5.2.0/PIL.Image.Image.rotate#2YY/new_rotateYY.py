from PIL import Image
img = Image.open('/home/zhang/example.jpg')
rotated_img = img.rotate(angle=45, fillcolor=None)
