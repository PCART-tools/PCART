import logging
from rich.logging import RichHandler
handler = RichHandler(logging.NOTSET, None, show_path=True, highlighter=None)
