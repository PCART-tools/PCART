import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, Console(), show_path=True, highlighter=ReprHighlighter(), show_level=True, tracebacks_extra_lines=3, enable_link_path=True, tracebacks_theme='monokai', show_time=True, markup=False, rich_tracebacks=True, tracebacks_width=80, tracebacks_show_locals=False)
