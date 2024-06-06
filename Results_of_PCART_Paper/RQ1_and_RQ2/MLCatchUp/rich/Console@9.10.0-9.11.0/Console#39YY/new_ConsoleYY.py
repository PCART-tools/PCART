from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(stderr=False, theme=Theme(), record=False, file=sys.stdout, force_terminal=False, tab_size=4, force_jupyter=False, color_system='auto', no_color=False, soft_wrap=False, width=80, height=25, style='bold red', markup=True, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
