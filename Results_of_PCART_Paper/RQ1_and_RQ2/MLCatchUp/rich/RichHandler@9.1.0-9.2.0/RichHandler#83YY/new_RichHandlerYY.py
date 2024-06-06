import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, Console(), show_level=True, show_time=True, highlighter=ReprHighlighter(), markup=False, enable_link_path=True, show_path=True, tracebacks_show_locals=False)
