from PIL import ImageOps, Image
image = Image.new('L', (100, 100), color='white')
black_color = '#000000'
white_color = '#FFFFFF'
result_image = ImageOps.colorize(image=image, black=black_color, white=white_color, mid=None, blackpoint=0, whitepoint=255, midpoint=127)
