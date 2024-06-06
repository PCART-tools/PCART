from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED
from rich import print
renderable = Text('Hello, World!', justify='center')
panel = Panel(style='none', padding=(0, 0), renderable=renderable, safe_box=None, width=None, expand=True, style='none', border_style='none')
