from rich.columns import Columns
from rich.text import Text
columns = Columns(padding=(0, 1), renderables=[Text('Column 1'), Text('Column 2')], width=20, title=None)
