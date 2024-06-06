import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(position='A1', conditional_formats=None, workbook=None, table_style=None, table_name=None, row_heights=None, column_totals=None, sparklines=None, dtype_formats=None, column_widths=None, column_formats=None)
