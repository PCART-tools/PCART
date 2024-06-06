import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(level=logging.INFO, show_time=True, highlighter=ReprHighlighter(), show_level=True, console=Console(), show_path=True, tracebacks_extra_lines=3, rich_tracebacks=True, enable_link_path=True, tracebacks_word_wrap=True, markup=False, tracebacks_theme='monokai', tracebacks_width=80, tracebacks_show_locals=False)
