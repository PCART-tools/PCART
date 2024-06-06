from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED
from rich import print
renderable = Text('Hello, World!', justify='center')
panel = Panel(style='none', safe_box=None, renderable=renderable, expand=True, width=None, style='none', border_style='none')
