import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, rich_tracebacks=True, tracebacks_width=80, tracebacks_theme='monokai', tracebacks_extra_lines=3, show_time=True, show_level=True, enable_link_path=True, markup=False, highlighter=ReprHighlighter(), show_path=True, tracebacks_show_locals=False)
