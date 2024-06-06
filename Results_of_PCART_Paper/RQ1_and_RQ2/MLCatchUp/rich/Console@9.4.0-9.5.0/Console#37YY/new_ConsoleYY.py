from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(record=False, width=80, emoji=True, highlighter=ReprHighlighter(), highlight=True, theme=Theme(), file=sys.stdout, log_time_format='[%X]', log_time=True, markup=True, force_terminal=None, tab_size=4, log_path=True, color_system='auto', force_jupyter=None, height=25, soft_wrap=False, stderr=False, style=None)
