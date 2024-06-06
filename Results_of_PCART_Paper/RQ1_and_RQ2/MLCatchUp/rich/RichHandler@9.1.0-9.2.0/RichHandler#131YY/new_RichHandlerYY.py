import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(level=logging.INFO, show_time=True, highlighter=ReprHighlighter(), show_level=True, enable_link_path=True, console=Console(), show_path=True, tracebacks_width=80, tracebacks_theme='monokai', rich_tracebacks=True, tracebacks_extra_lines=3, markup=False, tracebacks_show_locals=False)
