from PIL import Image, ImageDraw
image = Image.new('RGB', (5, 5), color='white')
draw = ImageDraw.Draw(image)
xy = (2, 2)
value = (255, 0, 0)
ImageDraw.floodfill(image, xy, value, thresh=0)
