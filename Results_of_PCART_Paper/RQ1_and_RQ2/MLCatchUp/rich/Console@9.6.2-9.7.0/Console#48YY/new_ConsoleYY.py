from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(file=sys.stdout, log_time_format='[%X]', log_path=True, width=80, force_terminal=None, get_time=datetime.now().timestamp, tab_size=4, get_datetime=datetime.now, record=False, theme=Theme(), _environ={}, highlighter=ReprHighlighter(), highlight=True, height=25, legacy_windows=None, stderr=False, safe_box=True, emoji=True, color_system='auto', markup=True, soft_wrap=False, force_jupyter=None, style='bold red', log_time=True, no_color=None)
