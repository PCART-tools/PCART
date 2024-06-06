from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(record=False, file=sys.stdout, style='bold red', log_path=True, tab_size=4, force_terminal=None, highlight=True, markup=True, width=80, log_time=True, emoji=True, force_jupyter=None, height=25, theme=Theme(), color_system='auto', soft_wrap=False, stderr=False, no_color=None)
