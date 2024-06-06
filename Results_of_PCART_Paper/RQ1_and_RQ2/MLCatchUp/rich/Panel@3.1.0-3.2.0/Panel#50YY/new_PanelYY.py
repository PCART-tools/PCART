from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED
from rich import print
renderable = Text('Hello, World!', justify='center')
panel = Panel(renderable=renderable, box=ROUNDED, safe_box=None, padding=(0, 0), width=None, expand=True, style='none', style='none', border_style='none')
