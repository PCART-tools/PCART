import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None, table_style=None, float_precision=3, dtype_formats=None, column_totals=None, row_heights=None, worksheet=None, position='A1', sparklines=None, table_name=None, conditional_formats=None, column_widths=None, column_formats=None)
