import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(row_heights=None, column_formats=None, has_header=True, dtype_formats=None, column_totals=None, sparklines=None, table_name=None, conditional_formats=None, float_precision=3, table_style=None, column_widths=None, position='A1')
