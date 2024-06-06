import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(float_precision=3, column_totals=None, conditional_formats=None, column_formats=None, column_widths=None, workbook=None, row_heights=None, has_header=True, position='A1', table_style=None, dtype_formats=None, sparklines=None, table_name=None)
