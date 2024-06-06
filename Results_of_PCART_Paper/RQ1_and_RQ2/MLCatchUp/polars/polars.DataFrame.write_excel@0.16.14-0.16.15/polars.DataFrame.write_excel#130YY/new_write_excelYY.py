import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None,  None, dtype_formats=None, table_style=None, position='A1', column_totals=None, float_precision=3, sparklines=None, table_name=None, column_widths=None, conditional_formats=None, row_heights=None, column_formats=None)
