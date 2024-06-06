import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(enable_link_path=True, level=logging.NOTSET, show_path=True, console=Console(), show_time=True, show_level=True)
