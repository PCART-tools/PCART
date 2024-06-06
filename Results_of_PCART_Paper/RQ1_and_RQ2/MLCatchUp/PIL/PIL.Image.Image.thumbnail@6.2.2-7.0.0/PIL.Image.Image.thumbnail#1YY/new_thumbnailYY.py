from PIL import Image
img = Image.open('/home/zhang/example.jpg')
img.thumbnail((100, 100), reducing_gap=2.0)
