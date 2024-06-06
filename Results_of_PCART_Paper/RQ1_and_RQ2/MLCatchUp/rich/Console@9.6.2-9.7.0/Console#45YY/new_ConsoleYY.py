from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(log_time=True, safe_box=True, file=sys.stdout, tab_size=4, theme=Theme(), soft_wrap=False, emoji=True, style='bold red', stderr=False, log_path=True, log_time_format='[%X]', record=False, force_jupyter=None, width=80, markup=True, legacy_windows=None, color_system='auto', highlighter=ReprHighlighter(), force_terminal=None, height=25, highlight=True, no_color=None)
