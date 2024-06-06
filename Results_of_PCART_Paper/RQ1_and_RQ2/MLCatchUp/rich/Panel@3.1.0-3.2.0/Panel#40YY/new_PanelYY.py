from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED
from rich import print
renderable = Text('Hello, World!', justify='center')
panel = Panel(renderable, safe_box=None, width=None, box=ROUNDED, expand=True, padding=(0, 0), style='none', style='none', border_style='none')
