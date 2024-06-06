from rich.columns import Columns
from rich.text import Text
columns = Columns(renderables=[Text('Column 1'), Text('Column 2')], padding=(0, 1), expand=False, width=20, title=None)
