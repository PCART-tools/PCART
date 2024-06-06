from rich.columns import Columns
from rich.text import Text
columns = Columns(column_first=False, padding=(0, 1), renderables=[Text('Column 1'), Text('Column 2')], title=None)
