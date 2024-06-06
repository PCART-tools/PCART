import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, highlighter=ReprHighlighter(), show_level=True, tracebacks_width=80, tracebacks_theme='monokai', markup=False, enable_link_path=True, show_time=True, console=Console(), tracebacks_extra_lines=3, show_path=True, rich_tracebacks=True, tracebacks_show_locals=False)
