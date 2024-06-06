import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(row_heights=None, table_name=None, table_style=None, autofit=False, autofilter=True, column_formats=None, position='A1', dtype_formats=None, column_widths=None, float_precision=3, sparklines=None, conditional_formats=None, column_totals=None, has_header=True)
