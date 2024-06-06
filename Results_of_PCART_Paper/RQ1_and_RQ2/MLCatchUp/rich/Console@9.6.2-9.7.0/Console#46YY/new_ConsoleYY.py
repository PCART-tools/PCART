from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(markup=True, safe_box=True, style='bold red', height=25, get_datetime=datetime.now, legacy_windows=None, width=80, soft_wrap=False, highlighter=ReprHighlighter(), highlight=True, force_jupyter=None, stderr=False, record=False, force_terminal=None, color_system='auto', log_time_format='[%X]', log_time=True, tab_size=4, emoji=True, theme=Theme(), file=sys.stdout, log_path=True, no_color=None)
