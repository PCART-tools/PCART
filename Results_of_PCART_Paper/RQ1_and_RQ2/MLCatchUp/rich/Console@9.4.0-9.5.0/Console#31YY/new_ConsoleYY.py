from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(record=False, force_jupyter=None, width=80, height=25, markup=True, file=sys.stdout, theme=Theme(), tab_size=4, color_system='auto', force_terminal=None, soft_wrap=False, stderr=False, style=None)
