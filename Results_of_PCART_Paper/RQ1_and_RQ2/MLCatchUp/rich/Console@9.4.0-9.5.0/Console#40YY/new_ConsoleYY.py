from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(log_time_format='[%X]', force_jupyter=None, markup=True, color_system='auto', emoji=True, safe_box=True, height=25, get_datetime=datetime.now, theme=Theme(), legacy_windows=None, file=sys.stdout, highlighter=ReprHighlighter(), log_path=True, force_terminal=None, width=80, record=False, highlight=True, tab_size=4, log_time=True, soft_wrap=False, stderr=False, style=None)
