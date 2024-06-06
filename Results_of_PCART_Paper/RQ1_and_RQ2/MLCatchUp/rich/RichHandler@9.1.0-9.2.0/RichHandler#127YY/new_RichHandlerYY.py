import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(highlighter=ReprHighlighter(), show_level=True, console=Console(), markup=False, show_time=True, level=logging.INFO, show_path=True, enable_link_path=True, tracebacks_show_locals=False)
