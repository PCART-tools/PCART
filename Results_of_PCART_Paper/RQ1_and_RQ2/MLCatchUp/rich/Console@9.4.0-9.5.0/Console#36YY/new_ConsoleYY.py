from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(force_jupyter=None, log_path=True, log_time_format='[%X]', force_terminal=None, tab_size=4, height=25, record=False, width=80, file=sys.stdout, theme=Theme(), emoji=True, color_system='auto', highlight=True, log_time=True, markup=True, soft_wrap=False, stderr=False, style=None)
