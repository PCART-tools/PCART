from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(file=sys.stdout, theme=Theme(), tab_size=4, force_jupyter=None, record=False, log_path=True, force_terminal=None, highlighter=ReprHighlighter(), height=25, markup=True, log_time_format='[%X]', emoji=True, width=80, color_system='auto', legacy_windows=None, log_time=True, highlight=True, soft_wrap=False, stderr=False, style=None)
