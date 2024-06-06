import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.NOTSET, console=Console(), highlighter=ReprHighlighter(), enable_link_path=True, show_path=True, show_time=True, show_level=True)
