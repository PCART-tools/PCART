from rich.columns import Columns
from rich.text import Text
columns = Columns(width=20, renderables=[Text('Column 1'), Text('Column 2')], padding=(0, 1), equal=False, expand=False, column_first=False, title=None)
