import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_level=True, show_path=True, show_time=True, enable_link_path=True, tracebacks_show_locals=False)
