from rich.columns import Columns
from rich.text import Text
columns = Columns(width=20, column_first=False, expand=False, padding=(0, 1), renderables=[Text('Column 1'), Text('Column 2')], align='center', equal=False, right_to_left=False, title=None)
