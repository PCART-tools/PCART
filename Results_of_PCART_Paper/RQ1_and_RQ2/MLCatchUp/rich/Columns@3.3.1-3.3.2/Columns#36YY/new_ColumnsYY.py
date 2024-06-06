from rich.columns import Columns
from rich.text import Text
columns = Columns(width=20, equal=False, align='center', expand=False, right_to_left=False, renderables=[Text('Column 1'), Text('Column 2')], column_first=False, title=None)
