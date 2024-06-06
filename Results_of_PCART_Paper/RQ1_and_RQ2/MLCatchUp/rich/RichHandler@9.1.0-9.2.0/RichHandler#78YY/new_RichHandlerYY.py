import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(logging.INFO, Console(), tracebacks_word_wrap=True, tracebacks_show_locals=False)
