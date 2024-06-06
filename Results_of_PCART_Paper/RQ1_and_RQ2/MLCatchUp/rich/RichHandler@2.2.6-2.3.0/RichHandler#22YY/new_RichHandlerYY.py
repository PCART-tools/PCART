import logging
from rich.logging import RichHandler
handler = RichHandler(show_path=True, console=None, level=logging.NOTSET, highlighter=None)
