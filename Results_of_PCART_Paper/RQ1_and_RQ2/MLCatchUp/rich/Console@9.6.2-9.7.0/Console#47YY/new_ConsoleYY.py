from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(force_jupyter=None, highlighter=ReprHighlighter(), height=25, color_system='auto', file=sys.stdout, highlight=True, safe_box=True, width=80, log_path=True, log_time=True, legacy_windows=None, markup=True, soft_wrap=False, get_datetime=datetime.now, force_terminal=None, record=False, stderr=False, tab_size=4, log_time_format='[%X]', style='bold red', get_time=datetime.now().timestamp, emoji=True, theme=Theme(), no_color=None)
