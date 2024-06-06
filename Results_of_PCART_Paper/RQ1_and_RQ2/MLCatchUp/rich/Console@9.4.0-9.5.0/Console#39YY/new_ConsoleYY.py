from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(emoji=True, legacy_windows=None, force_terminal=None, safe_box=True, height=25, theme=Theme(), highlighter=ReprHighlighter(), tab_size=4, log_time_format='[%X]', record=False, log_time=True, width=80, force_jupyter=None, highlight=True, file=sys.stdout, log_path=True, markup=True, color_system='auto', soft_wrap=False, stderr=False, style=None)
