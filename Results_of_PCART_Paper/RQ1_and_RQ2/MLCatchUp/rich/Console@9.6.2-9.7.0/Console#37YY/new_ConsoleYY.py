from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(record=False, height=25, soft_wrap=False, width=80, force_terminal=None, tab_size=4, stderr=False, color_system='auto', markup=True, style='bold red', theme=Theme(), file=sys.stdout, force_jupyter=None, no_color=None)
