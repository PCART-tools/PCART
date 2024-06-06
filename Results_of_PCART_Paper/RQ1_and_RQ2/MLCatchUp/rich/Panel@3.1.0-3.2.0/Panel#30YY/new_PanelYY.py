from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED
from rich import print
renderable = Text('Hello, World!', justify='center')
panel = Panel(renderable, ROUNDED, expand=True, style='none', width=None, safe_box=None, padding=(0, 0), style='none', border_style='none')
