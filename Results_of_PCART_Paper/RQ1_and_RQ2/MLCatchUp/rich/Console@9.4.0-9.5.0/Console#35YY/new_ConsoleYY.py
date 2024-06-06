from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(height=25, color_system='auto', force_jupyter=None, log_time=True, file=sys.stdout, width=80, tab_size=4, highlight=True, log_path=True, force_terminal=None, markup=True, record=False, emoji=True, theme=Theme(), soft_wrap=False, stderr=False, style=None)
