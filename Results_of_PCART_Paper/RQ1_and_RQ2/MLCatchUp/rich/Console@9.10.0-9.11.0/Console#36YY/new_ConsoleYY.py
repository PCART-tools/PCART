from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(style='bold red', force_jupyter=False, no_color=False, color_system='auto', soft_wrap=False, width=80, theme=Theme(), stderr=False, force_terminal=False, height=25, file=sys.stdout, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
