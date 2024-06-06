from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(color_system='auto', width=80, file=sys.stdout, force_terminal=None, tab_size=4, record=False, height=25, theme=Theme(), emoji=True, force_jupyter=None, markup=True, soft_wrap=False, stderr=False, style=None)
