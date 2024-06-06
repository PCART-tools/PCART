from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(log_time_format='[%X]', force_jupyter=None, height=25, log_path=True, width=80, file=sys.stdout, highlighter=ReprHighlighter(), get_datetime=datetime.now, tab_size=4, markup=True, record=False, highlight=True, theme=Theme(), log_time=True, force_terminal=None, color_system='auto', _environ={}, legacy_windows=None, get_time=datetime.now().timestamp, safe_box=True, emoji=True, soft_wrap=False, stderr=False, style=None)
