import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, enable_link_path=True, show_path=True, show_time=True, console=Console(), show_level=True, tracebacks_show_locals=False)
