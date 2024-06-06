import logging
from rich.logging import RichHandler
handler = RichHandler(enable_link_path=True, level=logging.NOTSET, show_path=True, highlighter=None)
