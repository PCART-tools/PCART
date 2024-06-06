import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(enable_link_path=True, level=logging.INFO, highlighter=ReprHighlighter(), rich_tracebacks=True, show_time=True, show_path=True, show_level=True, console=Console(), markup=False, tracebacks_show_locals=False)
