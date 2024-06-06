import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_path=True, level=logging.NOTSET, show_time=True, show_level=True)
