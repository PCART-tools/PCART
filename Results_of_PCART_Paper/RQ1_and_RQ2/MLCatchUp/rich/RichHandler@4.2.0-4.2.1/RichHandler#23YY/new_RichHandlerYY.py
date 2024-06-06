import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(level=logging.NOTSET, enable_link_path=True, show_path=True, highlighter=ReprHighlighter(), show_time=True, show_level=True)
