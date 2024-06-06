from PIL import EpsImagePlugin
eps_path = '/home/zhang/example.eps'
eps_image = EpsImagePlugin.EpsImageFile(eps_path)
eps_image.load(scale=1, transparency=False)
