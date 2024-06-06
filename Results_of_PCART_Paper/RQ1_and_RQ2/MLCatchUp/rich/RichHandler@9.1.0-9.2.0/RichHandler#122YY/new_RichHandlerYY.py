import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(tracebacks_word_wrap=True, console=Console(), level=logging.INFO, tracebacks_show_locals=False)
