import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(level=logging.INFO, markup=False, tracebacks_show_locals=False)
