import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(tracebacks_extra_lines=3, level=logging.INFO, tracebacks_show_locals=False)
