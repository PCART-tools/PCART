from rich.columns import Columns
from rich.text import Text
columns = Columns(right_to_left=False, column_first=False, renderables=[Text('Column 1'), Text('Column 2')], width=20, equal=False, padding=(0, 1), expand=False, title=None)
