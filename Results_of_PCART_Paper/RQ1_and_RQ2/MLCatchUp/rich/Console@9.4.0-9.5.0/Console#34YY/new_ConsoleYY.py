from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(height=25, color_system='auto', emoji=True, force_terminal=None, force_jupyter=None, file=sys.stdout, tab_size=4, markup=True, record=False, log_time=True, theme=Theme(), highlight=True, width=80, soft_wrap=False, stderr=False, style=None)
