import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, show_path=True, show_level=True, enable_link_path=True, tracebacks_extra_lines=3, tracebacks_width=80, rich_tracebacks=True, markup=False, console=Console(), highlighter=ReprHighlighter(), show_time=True, tracebacks_show_locals=False)
