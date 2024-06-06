import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(level=logging.INFO, tracebacks_extra_lines=3, console=Console(), tracebacks_show_locals=False)
