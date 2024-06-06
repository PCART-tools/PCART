from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(width=80, theme=Theme(), record=False, color_system='auto', style='bold red', force_terminal=None, tab_size=4, markup=True, emoji=True, file=sys.stdout, height=25, log_time=True, stderr=False, force_jupyter=None, highlight=True, soft_wrap=False, no_color=None)
