from PIL import Image
img = Image.open('/home/zhang/example.jpg')
bbox = img.getbbox(alpha_only=True)
