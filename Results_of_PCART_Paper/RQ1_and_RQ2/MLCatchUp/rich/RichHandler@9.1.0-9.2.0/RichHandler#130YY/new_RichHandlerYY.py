import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(rich_tracebacks=True, level=logging.INFO, console=Console(), show_time=True, markup=False, tracebacks_extra_lines=3, highlighter=ReprHighlighter(), show_level=True, enable_link_path=True, tracebacks_width=80, show_path=True, tracebacks_show_locals=False)
