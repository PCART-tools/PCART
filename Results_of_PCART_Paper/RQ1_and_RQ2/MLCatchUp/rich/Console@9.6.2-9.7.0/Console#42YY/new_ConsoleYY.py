from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(highlight=True, log_time=True, markup=True, theme=Theme(), force_jupyter=None, log_time_format='[%X]', soft_wrap=False, color_system='auto', style='bold red', file=sys.stdout, log_path=True, width=80, emoji=True, stderr=False, height=25, record=False, tab_size=4, force_terminal=None, no_color=None)
