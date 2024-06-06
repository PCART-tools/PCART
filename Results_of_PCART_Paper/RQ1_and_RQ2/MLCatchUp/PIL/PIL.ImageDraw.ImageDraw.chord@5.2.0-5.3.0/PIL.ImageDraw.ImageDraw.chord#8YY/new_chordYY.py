from PIL import Image, ImageDraw
image = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(image)
xy = [(50, 50), (150, 150)]
start = 0
end = 180
fill = 'blue'
outline = 'red'
draw.chord(xy, start=start, end=end, fill=fill, width=0)
