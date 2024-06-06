from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(tab_size=4, style='bold red', force_terminal=None, emoji=True, log_time=True, color_system='auto', force_jupyter=None, markup=True, highlight=True, log_path=True, theme=Theme(), log_time_format='[%X]', highlighter=ReprHighlighter(), record=False, height=25, stderr=False, soft_wrap=False, file=sys.stdout, width=80, no_color=None)
