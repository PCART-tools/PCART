from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(soft_wrap=False, stderr=False, file=sys.stdout, theme=Theme(), color_system='auto', force_jupyter=False, force_terminal=False, force_interactive=None, quiet=False, FormatTimeCallable]='[%X]')
