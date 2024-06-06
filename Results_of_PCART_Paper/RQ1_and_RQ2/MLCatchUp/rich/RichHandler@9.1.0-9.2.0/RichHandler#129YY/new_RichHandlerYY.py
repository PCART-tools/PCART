import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(enable_link_path=True, markup=False, rich_tracebacks=True, show_level=True, show_time=True, console=Console(), level=logging.INFO, show_path=True, highlighter=ReprHighlighter(), tracebacks_width=80, tracebacks_show_locals=False)
