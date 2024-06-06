from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(force_jupyter=False, color_system='auto', soft_wrap=False, force_terminal=False, theme=Theme(), width=80, stderr=False, file=sys.stdout, height=25, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
