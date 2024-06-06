import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, Console(), show_path=True, tracebacks_theme='monokai', markup=False, enable_link_path=True, rich_tracebacks=True, highlighter=ReprHighlighter(), show_level=True, tracebacks_width=80, tracebacks_word_wrap=True, show_time=True, tracebacks_extra_lines=3, tracebacks_show_locals=False)
