from rich.columns import Columns
from rich.text import Text
columns = Columns(column_first=False, equal=False, width=20, expand=False, renderables=[Text('Column 1'), Text('Column 2')], right_to_left=False, title=None)
