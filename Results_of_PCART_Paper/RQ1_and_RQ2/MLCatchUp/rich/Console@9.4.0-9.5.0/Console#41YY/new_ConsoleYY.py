from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(safe_box=True, height=25, log_time=True, highlighter=ReprHighlighter(), legacy_windows=None, theme=Theme(), markup=True, tab_size=4, get_time=datetime.now().timestamp, width=80, force_terminal=None, get_datetime=datetime.now, log_path=True, force_jupyter=None, record=False, emoji=True, file=sys.stdout, color_system='auto', highlight=True, log_time_format='[%X]', soft_wrap=False, stderr=False, style=None)
