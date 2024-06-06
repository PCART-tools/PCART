import logging
from rich.logging import RichHandler
handler = RichHandler(logging.NOTSET, None, enable_link_path=True, show_path=True, highlighter=None)
