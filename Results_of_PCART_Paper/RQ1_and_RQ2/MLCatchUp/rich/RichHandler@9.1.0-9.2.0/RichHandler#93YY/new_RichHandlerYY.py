import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, enable_link_path=True, console=Console(), tracebacks_show_locals=False)
